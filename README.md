# r1-computer-use

Applying the ideas of Deepseek R1 and [Open R1](https://github.com/huggingface/open-r1) to computer use.

<img src="./static/rac.svg" alt="diagram" width="500">

The primary challenge of this project is dealing with the soft-verifiable reward problem. In R1, they rely heavily on hard-verifiable rewards, which are not available at scale in real world GUI interactions.

We propose utilizing neural reward models as the verifier. 