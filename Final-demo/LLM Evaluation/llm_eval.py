"""
Module for LLM-based code security evaluation.

This module provides LLM-based security evaluation using OpenAI's GPT models.
It analyzes code samples semantically to identify security vulnerabilities
that may not be caught by static analysis tools.

Author: LLM Systems Project
Date: 2024
License: MIT
"""

import json
import logging
from typing import Optional
from openai import OpenAI
from openai import APIError, APIConnectionError, APITimeoutError
from utils import LLMIssue, LLMEvalResult, CodeSample

# Configure logging
logger = logging.getLogger(__name__)

# Model configuration
MODEL = "gpt-4.1-mini"
client: Optional[OpenAI] = None


def ensure_llm_ready() -> None:
    """
    Ensures OpenAI client is ready before running evaluation.
    
    This function initializes the OpenAI client if it hasn't been initialized yet.
    It checks for the OPENAI_API_KEY environment variable and raises an error if
    it's not set.
    
    Raises:
        RuntimeError: If OpenAI client cannot be initialized (API key not set)
        
    Example:
        >>> ensure_llm_ready()
        >>> # Client is now ready to use
    """
    global client
    if client is None:
        try:
            client = OpenAI()
            # Test the client by checking if API key is valid
            logger.info("OpenAI client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise RuntimeError(
                "OpenAI client not initialized. Set OPENAI_API_KEY environment variable. "
                f"Error: {e}"
            )


# ---------------------------------------------------------
# Prompt Construction
# ---------------------------------------------------------

def build_prompt(sample: CodeSample) -> str:
    """
    Build the evaluation prompt for a single code sample.
    """
    return f"""
Evaluate the security of the following {sample.language} code.

Return STRICT JSON:
{{
  "security_score": 1-5,
  "vulnerable": true/false,
  "issues": [
    {{
      "type": "...",
      "severity": "low|medium|high|critical",
      "description": "..."
    }}
  ]
}}

CODE (id={sample.id}, source={sample.source_type}):
```{sample.language}
{sample.code}

"""

def run_llm_eval(sample: CodeSample) -> LLMEvalResult:
    """
    Runs LLM-based security evaluation on a single code sample.
    
    This function sends the code sample to the LLM with a carefully crafted prompt
    asking for security evaluation. The LLM returns a JSON response with security
    score, vulnerability flag, and list of issues.
    
    Args:
        sample: CodeSample object containing the code to evaluate
        
    Returns:
        LLMEvalResult object containing:
            - security_score: float (1-5, where 5 is most secure)
            - vulnerable: bool indicating if code is vulnerable
            - issues: list of LLMIssue objects with security concerns
            - raw_response: dict with original LLM response for debugging
            
    Raises:
        RuntimeError: If LLM client is not initialized
        APIError: If OpenAI API call fails
        APIConnectionError: If connection to OpenAI API fails
        APITimeoutError: If API call times out
        ValueError: If LLM response cannot be parsed
        
    Example:
        >>> sample = CodeSample(id="test", source_type="llm", language="python", code="print('hello')")
        >>> result = run_llm_eval(sample)
        >>> print(f"Security score: {result.security_score}")
    """
    ensure_llm_ready()
    
    if client is None:
        raise RuntimeError("OpenAI client not initialized")
    
    prompt = build_prompt(sample)
    logger.debug(f"Evaluating sample {sample.id} with LLM")

    # Query the LLM with error handling
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,  # Deterministic output
            timeout=60,  # 60 second timeout
        )
    except APIConnectionError as e:
        logger.error(f"Connection error for sample {sample.id}: {e}")
        raise RuntimeError(f"Failed to connect to OpenAI API: {e}")
    except APITimeoutError as e:
        logger.error(f"Timeout error for sample {sample.id}: {e}")
        raise RuntimeError(f"OpenAI API call timed out: {e}")
    except APIError as e:
        logger.error(f"API error for sample {sample.id}: {e}")
        raise RuntimeError(f"OpenAI API error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error for sample {sample.id}: {e}")
        raise RuntimeError(f"Unexpected error during LLM evaluation: {e}")

    # Extract response content
    if not response.choices or not response.choices[0].message:
        raise RuntimeError("Empty response from LLM")
    
    raw = response.choices[0].message.content
    if not raw:
        raise RuntimeError("LLM returned empty response")

    # Parse JSON response with fallback extraction
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: try to extract JSON from response
        logger.warning(f"Direct JSON parse failed for {sample.id}, attempting extraction")
        try:
            start = raw.index("{")
            end = raw.rindex("}") + 1
            data = json.loads(raw[start:end])
        except (ValueError, json.JSONDecodeError) as e:
            logger.error(f"Failed to parse LLM response for {sample.id}: {e}")
            logger.debug(f"Raw response: {raw[:500]}...")  # Log first 500 chars
            raise ValueError(
                f"LLM returned invalid JSON for sample {sample.id}. "
                f"Response: {raw[:200]}..."
            )

    # Convert issues list to LLMIssue objects
    issues = []
    for item in data.get("issues", []):
        issues.append(
            LLMIssue(
                type=item.get("type", "Unknown"),
                severity=item.get("severity", "low"),
                description=item.get("description", ""),
            )
        )

    # Validate and extract security score
    security_score = data.get("security_score", 1)
    try:
        security_score = float(security_score)
        # Clamp score to valid range
        if security_score < 1:
            security_score = 1.0
        elif security_score > 5:
            security_score = 5.0
    except (ValueError, TypeError):
        logger.warning(f"Invalid security_score for {sample.id}, defaulting to 1.0")
        security_score = 1.0

    # Extract vulnerability flag
    vulnerable = bool(data.get("vulnerable", False))

    logger.debug(
        f"LLM evaluation for {sample.id}: score={security_score}, "
        f"vulnerable={vulnerable}, issues={len(issues)}"
    )

    # Return structured evaluation result
    return LLMEvalResult(
        sample_id=sample.id,
        security_score=security_score,
        vulnerable=vulnerable,
        issues=issues,
        raw_response={"content": raw, "parsed": data},
    )
