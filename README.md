# r1-computer-use

Applying the ideas of [Deepseek R1](https://github.com/deepseek-ai/DeepSeek-R1) and [Open R1](https://github.com/huggingface/open-r1) to computer use.

## Overview

The primary challenge of this project is providing robust enough reward signals to induce reasoning. R1 relies heavily on hard-verifiable rewards, which are not available at scale in real world GUI interactions.

R1-Computer-Use implements a novel architecture where both actor and reward models explicitly reason about computer interactions. Based on insights from DeepSeek-R1 and OpenR1, we demonstrate that explicit reasoning in both models leads to more robust and interpretable computer use.

## Architecture

Both models follow a three-step cycle which can be seen as an extention of [ReACT](https://react-lm.github.io/) into reinforcement learning.

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

## Usage

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

## Training

The training process focuses on developing strong reasoning patterns:

### Cold Start

- Expert demonstrations with reasoning traces
- Initial reward model training


### Reinforcement

- Rejection sampling on reasoning quality
- Dual model improvement loop


### Evaluation

- Task completion metrics
- Reasoning quality assessment
- Safety verification



## Research
Current areas of investigation:

- Reward model architectures
- Base model evaluations

## License
MIT

## Citation

@software{r1_computer_use,
  title     = {R1-Computer-Use: Reasoning-First Computer Interaction},
  author    = {Barker, Patrick},
  year      = {2025},
  url       = {https://github.com/agentsea/r1-computer-use},
}