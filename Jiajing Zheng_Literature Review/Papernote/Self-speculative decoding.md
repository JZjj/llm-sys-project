Draft & Verify: Lossless Large Language Model Acceleration via Self-Speculative Decoding
Jun Zhang, Jue Wang, Huan Li, Lidan Shou, Ke Chen, Gang Chen, Sharad Mehrotra

The introduction of the draft mode escalates the GPU memory overhead, increasing deployment challenges particularly on devices with restricted memory capacity.

Self-speculative decoding. Skipping certain layers in LLMs does not significantly compromise the generation quality. Selectively bypassing some intermediate layers. Use the LLM itself to generate draft tokens. 

Implementing self-speculative decoding poses two main challenges (a) determining which layers and the number of layers to skip during drafting, and (b) deciding the timing to stop generating draft tokens. We formulate it as an optimization problem, which accepts the combination of layers to bypass as input and aims to minimize the average inference time per token. We employ Bayesian optimization to solve this problem. The optimization is performed offline at the model level, and the searched layer combinations are fixed. To determine the optimal number of draft tokens (K) to generate. As shown in Figure 2, the choice of K significantly influences the end-to-end speedup: for an acceptance rate below 80%, a larger K is necessary. 
