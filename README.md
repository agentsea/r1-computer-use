# R1 Computer Use

Applying the ideas of [Deepseek R1](https://github.com/deepseek-ai/DeepSeek-R1) and [Open R1](https://github.com/huggingface/open-r1) to computer use.

## Overview

r1-computer-use is an experimental project that applies large-scale Reinforcement Learning techniques—similar to those outlined in DeepSeek-R1 to computer usage scenarios. The primary goal is to train an agent to interact with a computer environment (e.g., file system, web browser, command line) while utilizing a neural reward model to validate the correctness of the agent’s actions and reason about intermediate steps.

## Architecture

DeepSeek-R1 has shown that large language models can develop powerful reasoning skills through iterative reward optimization. Traditionally, such projects rely on hard verifiers or rule-based scripts to determine correctness in tasks like math or coding. However, these methods can be too narrow for more general, open-ended tasks such as “using a computer.”

We aim to replace hard-coded verifiers with a neural reward model that itself reasons about whether or not the agent’s actions are correct or helpful.

Both the actor and reward models follow a three-step cycle which can be seen as an extention of [ReACT](https://react-lm.github.io/) into reinforcement learning.

<img src="./static/rac.svg" alt="diagram" width="500">


## Agent

```python
observation = "Current directory contains: setup.py requirements.txt"
reasoning = """
1. Project appears to be a Python package
2. No virtual environment detected
3. Should create venv before proceeding
"""
action = "python -m venv .venv"
```

## Reward Model

```python
analysis = """
1. Correctly identified project type
2. Appropriate prerequisite check
3. Standard venv location chosen
"""
reward = 0.85
```

## Usage (in progress)

```python
from r1_computer_use import Agent, RewardModel

agent = Agent()
reward_model = RewardModel()

result = agent.run(
    task="Set up Python development environment",
    observe_reasoning=True
)

feedback = reward_model.evaluate(
    actions=result.actions,
    reasoning=result.reasoning
)
```

## Training Pipeline

The training pipeline consists of multiple stages:

1. **Cold Start**
   - Expert demonstrations with reasoning traces
   - Initial reward model training
   - Base model fine-tuning

2. **Reasoning-Focused GRPO**
   - Group-based sampling from current policy
   - Reward model evaluates each group
   - Compute advantages within groups
   - Policy updates with clipped probability ratios
   - KL divergence constraint with reference policy

3. **Rejection Sampling Stage**
   - Filter top-k solutions based on reward model
   - Create new training dataset from best examples
   - Fine-tune base model on filtered data

4. **General Preference Alignment**
   - Apply RL to full task distribution
   - Use reward models for general preferences
   - Focus on helpfulness and safety
   - Evaluate complete responses

5. **Evaluation**
   - Task completion metrics
   - Reasoning quality assessment 
   - Safety verification
   - Distribution shift analysis

## Roadmap

- [ ] Collect cold startand neural reward model data (in progress)
- [ ] SFT train base model
- [ ] GRPO RL training
- [ ] Rejection sampling
- [ ] General preference alignment
- [ ] Evaluation

## Research
Current areas of investigation:

- Reward model architectures
- Base model evaluations

## License
MIT

## Citation

```bibtex
@software{r1_computer_use,
  title     = {R1-Computer-Use: Reasoning-First Computer Interaction},
  author    = {Barker, Patrick},
  year      = {2025},
  url       = {https://github.com/agentsea/r1-computer-use},
}
```