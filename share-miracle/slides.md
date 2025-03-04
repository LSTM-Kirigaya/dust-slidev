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

# ShareMiracle
## 项目介绍

---
layout: table-of-contents
hideInToc: true
transition: slide-left
---
# 目录

---
transition: slide-left
---

# 项目背景

- **问题陈述**: 深度学习开发中数据处理和下载占用大量时间  (通常大于 70%)
- **解决方案**: 搭建统一的数据平台
- **目标用户**: 医学研究人员、数据科学家


<br>
<img src="https://pic1.zhimg.com/80/v2-18d7ebbe3715570cb348fb5321d92295_1440w.png" alt="Image 1" style="width: 200px">
<br>
<img src="https://picx.zhimg.com/80/v2-83e2016825bf5cfb2e83e34555c7542b_1440w.png" alt="Image 2" style="width: 200px">

---
transition: slide-left
---

# 项目目标

- **加速数据处理**: 减少数据处理和下载时间
- **统一数据平台**: 提供数据查询、下载和源头回溯功能
- **支持分布式深度学习**: 配合分布式算法加速模型训练

---
transition: slide-left
---

# 项目架构

- **前端**: 用户界面（数据展示、登录注册、数据标注）
- **后端**: Spring Boot 服务（数据管理、用户认证、数据导入）
- **数据库**: 存储元信息、用户信息、数据分级
- **数据存储**: 分布式存储系统（支持多种数据源）

---
layout: figure-side
figureUrl: https://picx.zhimg.com/80/v2-f37c4a50d3036ab273b0a2c54eb8b6d1_1440w.png
transition: slide-left
---

# 已完成功能

- **基础数据展示**: 数据查询、展示
- **登录注册**: 用户认证
- **元信息标注**: 数据唯一ID、数据源地址、数据简介
- **数据分级**: 任务、模态、器官


---
layout: figure-side
figureUrl: https://pica.zhimg.com/80/v2-96ed1ab121e446a12b204cbceefe273b_1440w.png
transition: slide-left
---

# 待开发功能

- JWT 令牌旋转更新
- 完整的数据展示和稳定的下载功能
- 数据导入功能: 支持 HTTP、FTP、Google Drive、百度网盘

---
layout: figure-side
figureUrl: https://pic1.zhimg.com/80/v2-24c7e7bd4e34e30200fc6aaccc68244c_1440w.png
transition: slide-left
---

# 技术栈

- **前端**: Vue.js
- **后端**: Spring Boot
- **数据库**: MySQL + ES
- **认证**: JWT

<br>

> 项目地址
>
> 前端： https://github.com/ShareMiracle/ShareMiracleFE
>
> 后端： https://github.com/ShareMiracle/ShareMiracleBE

---
transition: slide-left
---

# 项目部署与使用

- **部署环境**: 实验室内网环境
- **访问地址**: http://172.16.120.234:8081/data
- **使用说明**: 用户登录、数据查询、下载、标注


---
transition: slide-left
---

# Q & A

---
transition: slide-left
---