---
theme: academic
layout: cover
class: text-center
coverAuthor: 黄哲龙
fonts:
  local: Times, Montserrat, Roboto Mono, Roboto Slab
themeConfig:
  paginationX: r
  paginationY: t
  paginationPagesDisabled: [1]
title: 
hideInToc: true
transition: slide-left
---

# Deepseek R1
## Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

---
transition: slide-left
---

## Reinforcement learning from human feedback

<img src="https://pic1.zhimg.com/80/v2-92a81bb10f5591c19d68ac3b6ff4bd57_1440w.png" style="zoom:50%;" />

---
transition: slide-left
---

## Motivation

OpenAI's o1 marks a breakthrough in the reasoning ability LLM

![](https://pica.zhimg.com/80/v2-8c85967a9eba8bbb79f52bae67138d04_1440w.png)

- O1 has reached the level of a human expert in solving competition problems
- O1 has initially explored the second stage of AGI (Reasoner)


---
transition: slide-left
---

## Motivation

Pre-training may be coming to an end, but the Scaling Law will continue?

<img src="https://picx.zhimg.com/80/v2-5228ed1a661c54204b561880a72a8693_1440w.png" style="zoom:45%;" />

The new paradigm introduced by o1: Scale computation in reinforcement learning and inference

---
transition: slide-left
---

## Background

Reasoning Model based on Reinforcement Learning

Agent   =>  LLM

Action  =>   Next Token / Step / Solution

State    =>   LLM inputs 

Policy  =>  $\pi(\text{action} | \text{state})$

![](https://picx.zhimg.com/80/v2-8a6b0251ceb59e77dc56f5e97b4e0806_1440w.png)

---
transition: slide-left
---

## Related work

<img src="https://pic1.zhimg.com/80/v2-3693eaf83a9f3e2faa4d41e596808cad_1440w.png" style="zoom:45%;" />

---
transition: slide-left
---

## Policy Init

![](https://pica.zhimg.com/80/v2-533eff89f40bd4ae8a7873964b171608_1440w.png)

### Pre-training

Acquire basic logical reasoning and analytical skills through a large amount of mathematical and code texts that are rich in logic

### Supervision Fine-tuning
Further injecting human-like reasoning behaviors, with the ability to explore complex solution spaces


---
transition: slide-left
---

## Reward Design

Learning reward signals from the environment or human labels

<img src="https://picx.zhimg.com/80/v2-4722164b9edc62902c62aaa1a291c1bd_1440w.png" style="zoom:85%;" />

---
transition: slide-left
---

## Method

- DeepSeek-R1-Zero
    - Reinforcement Learning on the Base Model
- DeepSeek-R1
    - Reinforcement Learning with Cold Start


---
transition: slide-left
---

## DeepSeek-R1-Zero

Motivation: verify the effectiveness of inference(COT) in LLM training.

```mermaid
graph LR
database --> model(Deepseek V3)
model --> rule1(Rule One: Accuracy Rewards, \n Example: leetcode question with predefine UT)
model --> rule2(Rule Two: Format Rewards, \n enforce model to put its cot between `think` and `/think`)
rule1 --> score(merged scores)
rule2 --> score
score --feedback--> model
```

---
transition: slide-left
---

## PPO vs GRPO

### PPO

$$
\mathcal J_{PPO}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
$$

where


$$
r_t(\theta) = \frac{\pi_\theta (o_t | s_t)}{\pi_{\theta_{\text{old}}}(o_t | s_t)}
$$

### GRPO


$$
\mathcal J_{GRPO}(\theta) = \mathbb E\left[\sum_{i=1}^G\left(\min \left(\frac{\pi_\theta (o_i)}{\pi_{\theta_{\text{old}}}(o_i)}A_i, \mathrm{clip}(\frac{\pi_\theta (o_i)}{\pi_{\theta_{\text{old}}}(o_i)}, 1 - \epsilon, 1 + \epsilon)A_i\right) \\- \beta \mathbb D_{KL}(\pi_{\theta} || \pi_{ref})\right)\right]
$$

what you need to know

In large language models, GRPO removes the need for a separate value network, reducing memory and compute costs while aligning well with “comparative” Reward Model designs.

---
transition: slide-left
---

## Aha Moment

<img src="https://picx.zhimg.com/80/v2-2d76fa699b77c80edfdf728b5cedfc82_1440w.png" style="zoom:75%;" />

---
transition: slide-left
---

## DeepSeek-R1

Four step finetone

```mermaid
graph LR
model(Deepseek V3)

subgraph Training Pipeline
model --> step1(SFT)
step1 --> step2(RL)
step2 --> step3(Reasoning-\nOriented RL\nCheckpoint)
step3 --> step4(SFT)
step4 --> step5(RL)
end

subgraph Database
database1(Long COT Data\n `K Samples`)
database2(Reasoning: \nCoT, Math, etc. \n`144K samples`)
database3(Reasoning Data \n `600K samples`)
database4(Non-Reasoning\n Data \n `200K samples)
end

database1 --> step1
database2 --> step2
step3 --> database3
database3 --> step4
database4 --> step4
```


---
transition: slide-left
---

## Infra

### DP TP PP

![](https://picx.zhimg.com/80/v2-bfd04ba1f7d3447c5531b273346cadea_1440w.png)

> Colossal-AI: A Unified Deep Learning System For Large-Scale Parallel Training

---
transition: slide-left
---

## Dense -> PP

Gpipe

![](https://s2.loli.net/2022/01/28/OAucPF6mWYynUtV.png)

---
transition: slide-left
---

## Dense -> PP

1F1B

![](https://s2.loli.net/2022/01/28/iJrVkp2HLcahjsT.png)

---
transition: slide-left
---


## MOE -> EP

![](https://pica.zhimg.com/v2-402cba381f26a1ea46ea479772ea321c_r.jpg?source=c8b7c179)

> Outrageously Large Neural Network

---
transition: slide-left
---

## Reference

- [Scaling of Search and Learning: A Roadmap to Reproduce o1 from Reinforcement Learning Perspective](https://arxiv.org/pdf/2412.14135)

- [（夜话deepseek引用）强化学习与推理完美融合：o1技术路线图全揭秘-A Roadmap to Reproduce o1 from RL Perspective](https://zhuanlan.zhihu.com/p/21253947140)
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948)
- [DeepSeek-R1 Dissection: Understanding PPO & GRPO Without Any Prior Reinforcement Learning Knowledge](https://huggingface.co/blog/NormalUhr/grpo)
- [DeepSeek-R1训练过程](https://deepseek.csdn.net/67bdac1c2e30c8639006515b.html)

---
transition: slide-left
---

Q & A