---
theme: academic
layout: cover
class: text-center
coverAuthor: Zhelong Huang
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

# Paper Reading

## APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets

---
transition: slide-left
---

## Tool Usage: LLm -> Agent

**Background & Current Status**

* LLMs can autonomously invoke tools (e.g., weather APIs, calculators, databases, REST APIs), enabling real-time code execution ([proceedings.neurips.cc][1]).
* Widely applicable across domains like social networking, finance, travel, etc.

![](https://picx.zhimg.com/80/v2-b8933f8d808c0d4c54c75c94b3455fbe_1440w.png)

---
transition: slide-left
---


## Tool Usage: LLm -> Agent

**Major Challenges**

* **Data Quality**: Training data is static, noisy, and lacks accurate execution results.
* **Generalization to Unseen APIs**: Poor adaptability to new APIs.
* **Complex Calling Chains**: Difficulties with parallel/serial calls and semantic dependencies.

New Problems: Lack of function calling

---
transition: slide-left
---

## Prior Work on Tool-Using Agents & Datasets

**Representative Work**

* Toolformer: Fine-tunes LLMs to invoke tools like QA, calculator, and search ([arxiv.org][2]).
* RestGPT, xLAM, Octopus-v4, Gorilla: Multi-stage tool-using agents ([proceedings.neurips.cc][1]).
* Existing datasets: AgentInstruct, APIBank, Toolalpaca, ToolBench, etc.

<br>
<br>
<br>

```mermaid
graph RL
    A[User Query] --> B[LLM parses intent]
    B --> C[Agent Plans Tool Usage]
    C --> D1[Tool 1 Call]
    C --> D2[Tool 2 Call]
    D1 --> E[Result Aggregation]
    D2 --> E
    E --> F[Final Response Generation]
```

---

## Shortcomings in Existing Work

* **Lack of Validation**: Many datasets are auto-generated without execution or semantic checks — high noise.
* **Limited Scale**: Too few API types or calling scenarios.
* **Lack of Call Chain Complexity**: No support for realistic multi-function chains (e.g., parallel/serial usage).

---

## APIGen: A New Approach to Address These Gaps

**Core Contributions**

* Proposes APIGen — an automated pipeline with three-stage verification: format, execution, and semantic validation ([proceedings.neurips.cc][3]).
* Collects 3,673 executable APIs across 21 categories, generating 60,000 high-quality samples.

---

## APIGen: A New Approach to Address These Gaps

**Verification Strategies**

1. **Format Checking**: Ensures JSON, function signatures, etc., are valid.
2. **Live Execution**: Executes real API calls to validate responses.
3. **Semantic Matching**: Checks if the response aligns with the natural language prompt.

<br>
<br>
<br>

```mermaid
flowchart LR
    A[Generated Function Call] --> B[Stage 1: Format Checker]
    B -->|Valid JSON<br>Has query/answer/thought<br>Valid API + Args| C[Stage 2: Execution Checker]
    B -->|Invalid format or args| X1[Discarded]

    C -->|Executes successfully| D[Stage 3: Semantic Checker]
    C -->|Execution failed<br>TypeError, Timeout, etc.| X2[Discarded]

    D -->|Semantically aligned<br>Query matches results| E[High-Quality Data Saved]
    D -->|Infeasible / Irrelevant result| X3[Discarded]
```

---

## Experiment

**Main Objectives**

- How much can the generated data improve a model's function-calling capabilities?

- How effective is the APIGen framework in filtering out low-quality data?

---

## Experiment

**Experimental Approach**

Two base models were trained:
- DeepSeek-Coder-1.3B-instruct
- DeepSeek-Coder-7B-instruct-v1.5

Both used the xLAM (Large Action Model) training pipeline.

Resulting models are named:
- xLAM-1B (FC)
- xLAM-7B (FC)

---

## Experiment

**Comparison Targets**

Benchmarked against several state-of-the-art models:
- GPT-4 series (e.g., GPT-4o)
- Claude-3 series
- Gemini series
- LLaMA3
- Mixtral
- OpenFunctions-v2
- Command R+, etc.

---



## Experiment

**Comparison Targets**

<img src="https://pica.zhimg.com/80/v2-48615e75aa756b6e629fd8437bc396c1_1440w.png" width="70%" />

> NOTE: DeepSeek-Coder-v1.5 ranks 45th

---


## Experiment

**Ablation Study**

<img src="https://pic1.zhimg.com/80/v2-d31a839a6068dae5234ed3beea9594c0_1440w.png" width="50%" />


---

## Outlook: Towards MCP (Multi‑Call Planning)

**Future Directions**

* **Nested Call Chains**: Supports complex multi-level API usage. NESTFUL shows current accuracy is only 25% ([arxiv.org][5]).
* **Dialogue-Level Evaluation**: CONFETTI evaluates multi-turn function-calling, which still underperforms ([arxiv.org][6]).
* **MCP Vision**: Toward agents that plan multi-round, hybrid API calls with consistent intent understanding and logic.

---

## MCP

**What is MCP**

[OpenMCP](https://kirigaya.cn/openmcp/)

<img src="https://picx.zhimg.com/70/v2-1a2df8a081a76f4e90431d8a2445f495_1440w.avis" width="70%" />

---

## MCP

**Drawbacks**

- Lack of metrics
- Lack of design boundary (What it can do and can't)
- How to combine different mcp servers ? (tool description align)

---

## Reference

[1] https://proceedings.neurips.cc/paper_files/paper/2024/file/61cce86d180b1184949e58939c4f983d-Paper-Datasets_and_Benchmarks_Track.pdf

[2] https://arxiv.org/abs/2409.00920

[3] https://proceedings.neurips.cc/paper_files/paper/2024/hash/61cce86d180b1184949e58939c4f983d-Abstract-Datasets_and_Benchmarks_Track.html

[4] https://arxiv.org/abs/2406.18518

[5] https://arxiv.org/abs/2409.03797

[6] https://arxiv.org/abs/2506.01859

