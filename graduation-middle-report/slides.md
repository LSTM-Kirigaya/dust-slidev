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

# 毕设中期答辩
## 基于Diffusion的图像去噪算法

<Footnotes separator>
    <Footnote>南京航空航天大学 毕设答辩</Footnote>
</Footnotes>

---
layout: table-of-contents
hideInToc: true
transition: slide-left
---
# 大纲

<Footnotes separator>
    <Footnote>大纲</Footnote>
</Footnotes>

---
transition: slide-left
---

# 目前已经完成的部分

1. 调研并下载常用的图像去噪数据集（合计6.5G），完成数据集的搜索工作，编写完成数据集的加载模块。

<br>

- CBSD68
<br>

- SIDD_Small_sRGB_Only
- urban100

<Footnotes separator>
    <Footnote>目前已经完成的部分</Footnote>
</Footnotes>


---
transition: slide-left
---


2. 复现主要去噪的 SOTA 模型，并计算在标准数据集上的指标（PSNR,SSIM）

<br>

数据集: set5

| model | PSNR (db) | SSIM |
| --- | --- | --- |
| ffdnet | 35.17 | 0.9328 |
| dncnn_25 | 34.31 | 0.9173 |
| dpsr_x4_gan | 27.28 | 0.7921 |
| swinIR (SOTA) | 37.81 | 0.9539 |

> 对于denoise任务，PSNR和SSIM都是越大性能越好

<Footnotes separator>
    <Footnote>目前已经完成的部分</Footnote>
</Footnotes>

---
transition: slide-left
---

SwinIR表现：

![](https://picx.zhimg.com/80/v2-02c8e895f66eeb9f696541d03bee0ba7_1440w.png)

<Footnotes separator>
    <Footnote>目前已经完成的部分</Footnote>
</Footnotes>

---
transition: slide-left
---


3. 使用标准 img2img 的 diffusion 和 repaint 网络进行图像去噪初探。

<br>

![](https://picx.zhimg.com/80/v2-15c848a68ff5e1ad9120c7ed338af9f7_1440w.png)

<center>alt-diffusion, step=50</center>

<Footnotes separator>
    <Footnote>目前已经完成的部分</Footnote>
</Footnotes>

---
transition: slide-left
---

![](https://picx.zhimg.com/80/v2-04f324c05af168ead3a37e9e84ee94f9_1440w.png)

<center>GLIDE, RePaint</center>


<Footnotes separator>
    <Footnote>目前已经完成的部分</Footnote>
</Footnotes>

---
transition: slide-left
---

4. 设计针对于图像去噪的 Diffusion 的改进模型

![](https://picx.zhimg.com/80/v2-cfeadbc6f33fde845b3da518af1db8a7_1440w.png)


---
transition: slide-left
---

# 待完成的主要内容

1. 根据设计思路，训练并测试去噪 Diffusion 网络。
<br>

2. 整理实验结果，与 SOTA 比较，进行重复实验。
3. 基于实验结果设计并开发在线版本的图像去噪软件。
4. 根据实验结果，撰写论文。

<Footnotes separator>
    <Footnote>待完成的主要内容</Footnote>
</Footnotes>

---
transition: slide-left
---

# 存在的问题和解决办法

- 问题：Diffusion 生成图像容易破坏原图结构，需要约束 diffusion 的生成空间。

- 解决方法：
    1. 设计一种用于描述图像结构的、可导的度量，用于改进训练 diffusion 的损失函数。采用类似于 GLIDE 的思路，引入图像专属信息用于约束生成图像的空间。
    2. 弱化加噪的前向过程，从而控制去噪程度。


<Footnotes separator>
    <Footnote>存在的问题和解决办法</Footnote>
</Footnotes>


---
layout: cover
class: text-center
coverBackgroundUrl: 
hideInToc: true
transition: slide-left
---
# 感谢观看
## Q&A