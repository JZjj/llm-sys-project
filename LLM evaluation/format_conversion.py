import json

# Input file path
input_file = "/content/llm-sys-project/LLM evaluation/test.jsonl"
# Output file path
output_file = "/content/llm-sys-project/LLM evaluation/test_converted.jsonl"

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for idx, line in enumerate(f_in, 1):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            print(f"Warning: Failed to parse line {idx}")
            continue

        # Construct new JSON structure
        new_entry = {
            "id": f"c{idx}",
            "source_type": "github",
            "language": "python",
            "code": data.get("text", "")
        }

        # Write to the new file
        f_out.write(json.dumps(new_entry, ensure_ascii=False) + "\n")

print(f"Conversion finished. Output saved to {output_file}")
