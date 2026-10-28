# 远处 ELSEWHERE · 宇宙观察笔记

> 具有现代美术馆展览气质的单文件互动式天文探索展馆 · A Museum-Grade Interactive Astrophysics & Deep Space Exhibition

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#)
[![Zero-Dependency](https://img.shields.io/badge/Dependencies-Zero-success.svg)](#)
[![Single-File](https://img.shields.io/badge/Format-Standalone_HTML5-orange.svg)](#)
[![Audio](https://img.shields.io/badge/Engine-Web_Audio_API-purple.svg)](#)
[![Imagery](https://img.shields.io/badge/Imagery-NASA%20%7C%20ESA%20%7C%20EHT-0b3d91.svg)](#)

---

## 展览概览

《远处 ELSEWHERE》是一个融合现代视觉设计、天体物理严谨性与交互体验的数字天文展馆。摒弃了传统科普网页常见的杂乱星云叠加粗体大字，全站以墨黑与深空冷灰为画布，以真实科学影像为主角，构建起兼具美术馆策展质感与沉浸交互的数字展厅。

- **100% 离线单文件**：零外部 CDN、API 或字体请求，所有样式、矢量图标与 18 幅经过色彩标定的 NASA / ESA / EHT 真实深空任务影像均已内嵌（Base64）。
- **纯代码环境原声引擎**：基于原生 Web Audio API，利用振荡器与双二阶滤波器实时合成 55Hz 深空低频无人机环境原声（Cosmic Sub-bass Drone）与极简 UI 微音效。
- **全端自适应响应**：从 4K 宽屏到手机竖屏，所有排版、字体层级与交互控件均经过精确适配，文字边缘无锯齿，阅读对比度完全符合 WCAG AAA 标准。

---

## 九大主题展厅

| 展厅编号 | 展厅名称 | 核心展品与交互功能 |
| :---: | :--- | :--- |
| **00** | **策展总引 · 导览开篇** | 卡西尼号真实土星自然色合成影像、全展厅快速导航 Dock、多层视差星空粒子流、实时天球坐标（RA/DEC）与空间遥测 HUD、环境原声/动效全局开关 |
| **01** | **太阳系行星标本展台** | 水星至海王星 8 大行星可切换展签、真彩色标本碟、真实物理尺寸比例标尺、主要大气组分徽章、人类探测器先锋里程碑 |
| **02** | **卫星群与冰下海洋** | 木卫二、木卫三、土卫二、土卫六、月球 5 大卫星相对大小标本架、冰下海洋与羽状喷流剖析、交互式物理月相与晨昏线模拟器（0 ~ 29.5天连续拖动） |
| **03** | **恒星生命与核聚变谱系** | 从分子云坍缩到黑洞/白矮星的 5 阶段恒星演化时光轴、核心形态演变动画、哈佛光谱 O/B/A/F/G/K/M 恒星表面温度与颜色实时调谐器 |
| **04** | **星云专属展厅与多波段宇宙** | 詹姆斯·韦布空间望远镜 (JWST) 船底座 NGC 3324“宇宙悬崖”宽幅全景、3 处微观恒星育婴室细节标注、可见光/近红外/中红外/X射线四波段光谱实时滤镜切换 |
| **05** | **极端引力特展：黑洞与时空弯曲** | 事件视界望远镜 (EHT) M87* 超大质量黑洞阴影、相对论多普勒集束效应解析、实时引力透镜光线弯曲物理模拟画布（支持拖拽光线偏折） |
| **06** | **宜居地平线：系外行星寻觅** | TRAPPIST-1 红矮星系统七行星阵容、凌日法（Transit Method）恒星亮度衰减与光变曲线实时模拟器、系外大气分子吸收光谱谱线分析 |
| **07** | **宇宙尺度与人类深空舰队** | 从地月 1.3 光秒到可观测宇宙边缘 134 亿光年的光程时空穿越跳板、人类深空探测器（旅行者1号/2号、新视野号、帕克号、韦布、嫦娥/天问）编年史与遥测面板 |
| **08** | **观星实操、波特尔暗空模拟器与便笺** | 波特尔暗空分类法（Bortle 1~9级）夜空光害物理模拟器、4 步肉眼观星指南、支持本地 `localStorage` 自动持久化保存与 JSON/Markdown 导出的深空观察便笺 |
| **09** | **科学直觉测验实验室** | 8 道天体物理与太空探索经典思维自测题，点击选项即时提供理论解析与纠错反馈 |

---

## 快速运行与使用

### 1. 直接运行
无需任何服务器环境或编译步骤，直接在浏览器中打开：
- 根目录入口：`index.html`（支持直接部署至 GitHub Pages）
- 官方独立交付：`outputs/远处-宇宙观察笔记.html`

### 2. 源码构建与维护
若需要修改样式、内容或增补真实天体素材，可通过模块化源码重新构建：

```bash
# 进入构建目录
cd src

# 执行编译（读取 assets 目录真实影像，自动 Base64 编码并组合 CSS/JS 生成单文件）
python3 assemble.py
```

---

## 真实科研影像来源与致谢

全展厅所有天体摄影与科研数据均来源于权威深空探测任务官方公开档案：
- **土星 (Saturn)**: NASA / JPL-Caltech / Space Science Institute (*Cassini Equinox Mission*, PIA06193)
- **地球 (Earth)**: NASA / Apollo 17 Crew (*The Blue Marble*, AS17-148-22727)
- **船底座星云“宇宙悬崖” (Cosmic Cliffs)**: NASA, ESA, CSA, and STScI (*James Webb Space Telescope*, STScI-2022-031)
- **M87\* 超大质量黑洞 (M87\* Black Hole)**: Event Horizon Telescope Collaboration (EHT, PIA23122)
- **TRAPPIST-1 行星系统**: NASA / JPL-Caltech (PIA21422)
- **旅行者号深空探测器 (Voyager)**: NASA / JPL (PIA04495)
- 水星、金星、火星、木星、天王星、海王星、木卫二、土卫二等高分辨率真实标本切片均由 NASA Planetary Data System 与 USGS Astrogeology Science Center 处理提供。

---

## 开源协议

本项目代码与排版设计采用 [MIT License](LICENSE) 开源；天体影像与天文摄影版权归属原署名航天局（NASA / ESA / CSA / STScI / EHT Collaboration）所有，遵循其各自公开学术传播使用规范。
