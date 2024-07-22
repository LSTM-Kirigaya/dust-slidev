---
theme: academic
layout: cover
class: text-center
coverAuthor: 黄哲龙
coverAuthorUrl:  
coverBackgroundUrl: 
coverBackgroundSource: 
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

# Huggingface 介绍
## 医学多模态大数据建设 meeting 0.0.1

---
layout: figure-side
figureUrl: https://picx.zhimg.com/80/v2-4bc4172a00316a6db232e8cc71121b1e_1440w.png
transition: slide-left
---

## 什么是HuggingFace ？

<br>

> huggingface 在业界被简称为 HF 


<br>

- `Models`: 提供上传模型的平台和统一的下载、调用接口（最有名的功能，最近提供了模型压缩和量化的功能）
<v-click>

- `Datasets`: 数据集平台，提供统一的数据集下载接口（类似于Kaggle，但社区知名度有限，主流数据还是得靠网盘下载）
</v-click>

<v-click>

- `Spaces`: 提供免费或是付费的模型部署平台（类似于colab，正经企业还是选择自己买机器，所以难推）
</v-click>

<br>

<v-click>

**总结：HF是一个提供机器学习B端服务的平台**

</v-click>

---

## 为什么需要 HF ？

业界和学界的一大痛点
- 我想要快速实现深度学习算法来解决我的业务！
- 但是要自己配环境好麻烦！

<v-click>

HF：我们提供统一的平台、统一的下载函数和规范的开发环境！

</v-click>


<v-click>

- 我想要实现语音合成！
- 但是我不懂声码器和隐马尔科夫链！
- 大佬的文档我也看不懂！

</v-click>

<v-click>

HF：我们提供统一的接口函数和说明文档，你只需要调用函数！

</v-click>

---

## 为什么需要 HF ？

<br>

### 传统实现深度学习算法的步骤

1. STFW，用sentiment或者TTS为关键字搜索对应的项目
2. 找到可行的项目git clone
3. 根据README，配置环境、下载数据集、启动训练
4. 完成训练，进行性能测试，不行重训
5. 优化模型（压缩、量化、剪枝）
6. 进行部署（ONNX，TensorRT，TF）


<v-click>

> 很麻烦！
> - 项目年久失修了怎么办？
> - 数据集下载链接过期了怎么办？
> - 本地环境炸了怎么办？

</v-click>

---

## 具体怎么做的？

通过python库和提供在线下载服务

```bash
$ pip install transformers
```

<br>

<v-click>

### from_pretrained is all you need

- `from_pretrained`是一个具有网络下载功能的函数，它返回下载得到的HF模型。
- 相同领域任务的HF模型往往都有着完全相同的推理接口。

</v-click>

---

### 例子：五行实现一个情感分类器算法

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("techthiyanes/chinese_sentiment")
model = AutoModelForSequenceClassification.from_pretrained("techthiyanes/chinese_sentiment")

input_ids = tokenizer('今天天气真不错', return_tensors='pt')
print(input_ids)
```

输出：
```python
{'input_ids': tensor([[ 101,  791, 1921, 1921, 3698, 4696,  679, 7231,  102]]), 'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1]])}
```

---

## HF 的 缺点

<br>

### 网速！

有的地方下载非常不稳定，特别是模型比较大，每次下不完就会断开。手动下载模型在许多实验室已经成为一种常态。逐渐和原本的模式背离。

<v-click>

### 训练！

HF模型通过bin保存，原理上可以反编译，但是实际操作中，基于HF下载的模型重新训练非常麻烦。

</v-click>