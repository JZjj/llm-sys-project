SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding

Reading Note:

This framework is built around a draft-then-verify procedure: a small drafter model proposes multiple tokens, and a heavier verifier model evaluates the proposal in parallel to accept the longest matching sequence. However, the realized speedup depends on two key factors: the drafter latency and the drafter-verifier alignment

SpecDiff 2 leverage diffusion language models as non-autoregressive drafters to address bottleneck and develops novel alignment mechanism to calibrate diffusion drafter with verifiers at train and test-time, addressing bottleneck (2).

Discrete diffusion models generate text by iteratively transitioning the token space toward a fluent sequence in a small, fixed number of steps. Discrete diffusion models generate text by iteratively transitioning the token space toward a fluent sequence in a small, fixed number of steps. Each denoising step updates all token positions in parallel, so the drafting cost depends primarily on the number of steps rather then the sequence length.

However, diffusion drafters and autoregressive verifiers produce fundamentally different objects. Diffusion models learn a joint distribution over entire sequences through denoising trajectories, whereas autoregressive models learn local next-token conditionals tied to causal prefixes.
