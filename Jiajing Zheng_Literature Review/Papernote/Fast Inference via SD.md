Yaniv Leviathan, Matan Kalman, Yossi Matias Proceedings of the 40th International Conference on Machine Learning, PMLR 202:19274-19286, 2023.

Hard language-modeling tasks often include easier subtasks that can be approximated well by more efficient models, and using speculative execution and a novel sampling method

Not all inference steps are born alike - some require a very large model, while others can be approximated well by more efficient models. These adaptive computation methods aim to use less compute resources for easier inference steps. 

A well known example of speculative execution is branch prediction. Foe speculative execution to be effective, we need an efficient mechanism to suggest tasks to execute that are likely to be needed.

Speculative execution is an optimization technique, common in processors, where a task is performed in parallel to verifying if it is actually needed. - branch prediction. Speculative sampling, while guaranteeing that the output from our system have the same distribution as those from the target model alone.

A example of the first line, the target model only run once but 5 tokens were generated. 

The core idea is to use the more efficient model M_q to generate a completions (the parameter will be chosen) then use the target model Mp to evaluate all of the guesses and their respective probabilities from Mq in parallel, accepting al those that can lead to identical distribution.
