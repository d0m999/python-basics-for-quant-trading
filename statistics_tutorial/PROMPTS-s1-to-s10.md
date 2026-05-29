# 10 个 Session 直接可实施提示词

> 基于 PDF OCR 提取的目录结构，2026-05-29
> 书籍路径：/Users/d0m999/Desktop/_rag/基础统计学(第14版)[带书签扫描版].pdf
> 规范文件：.claude/skills/stats-notebook-tutorial.md

---

## 通用前置说明

每个 prompt 执行前，agent 必须：

1. **先读原书章节**：用 pdfplumber + pytesseract OCR 提取对应页码的文本，理解章节的公式、逻辑、例题
2. **再读参考 notebook**：读取 statistics_tutorial/ 下已有教程的风格（若无则参考 quant_tutorial/）
3. **最后编写教程**：严格遵循 stats-notebook-tutorial.md 规范

```python
# 通用 OCR 读取模板（每个 prompt 开头执行）
import pdfplumber
from PIL import Image
import pytesseract

pdf_path = "/Users/d0m999/Desktop/_rag/基础统计学(第14版)[带书签扫描版].pdf"

with pdfplumber.open(pdf_path) as pdf:
    for i in range(START-1, END):  # 页码从 0 开始
        page = pdf.pages[i]
        img = page.to_image(resolution=200)
        img_path = f"/tmp/page_{i+1}.png"
        img.save(img_path)
        text = pytesseract.image_to_string(img_path, lang='chi_sim+eng')
        if text and len(text.strip()) > 30:
            print(f"\n=== Page {i+1} ===")
            print(text[:2000])
```

---

## S1: Ch2 数据探索 + Ch3 集中趋势

```
为《基础统计学(第14版)》第 2-1、2-2 和 3-1 节编写 3 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
书籍路径：/Users/d0m999/Desktop/_rag/基础统计学(第14版)[带书签扫描版].pdf

需要 OCR 的页面范围（根据目录页码推算）：
- 2-1 频数分布表：约 p.33-42
- 2-2 直方图：约 p.43-50
- 3-1 集中趋势：约 p.71-74

通读后梳理：核心公式、计算步骤、例题类型、软件输出解读。

## 第二步：参考已有教程风格

读取 quant_tutorial/2.1-portfolio-sorts-tutorial.ipynb 了解风格。
读取 .claude/skills/stats-notebook-tutorial.md 了解规范。

## 第三步：编写教程

### Notebook 1: statistics_tutorial/2.1-frequency-distribution-tutorial.ipynb

主题：频数分布表——数据的整理与汇总

教学目标（5条）：
1. 理解频数分布表的结构：类别、频数、相对频数、累积频数
2. 掌握频数分布表的构建步骤：确定组数 → 组距 → 统计频数
3. 在微型数据集（20 个数据点）上手算频数分布表
4. 扩展到 500 个数据点，用 pandas 完成频数统计
5. 理解相对频数和累积频数在数据探索中的作用

参考原书要点：
- 洛杉矶每日通勤时间频数分布表
- 空难原因频数分布表（分类数据）
- 频数分布表的构建规则

### Notebook 2: statistics_tutorial/2.2-histogram-tutorial.ipynb

主题：直方图与正态分位图

教学目标（5条）：
1. 理解直方图与频数分布表的关系
2. 掌握直方图的绘制方法和参数选择（组数、组距）
3. 学会用直方图判断数据分布形态（对称、右偏、左偏）
4. 理解正态分位图（QQ plot）的原理和解读
5. 用 scipy.stats.probplot 绘制 QQ 图并判断正态性

参考原书要点：
- 直方图的基本概念
- 使用正态分位图评估正态性
- 不同分布形态的直方图特征

### Notebook 3: statistics_tutorial/3.1-central-tendency-tutorial.ipynb

主题：集中趋势的度量指标

教学目标（5条）：
1. 理解均值、中位数、众数的定义和计算方法
2. 掌握不同分布形态下集中趋势指标的选择策略
3. 手算 10 个数据点的均值、中位数、众数
4. 用 scipy 验证手算结果，扩展到 500 个数据点
5. 理解加权均值和截尾均值的应用场景

参考原书要点：
- 均值公式：$\bar{x} = \frac{\sum x_i}{n}$
- 中位数的确定方法（奇数/偶数个数据）
- 众数的定义和多峰情况
- 均值 vs 中位数在偏态分布中的差异

共同规范：
- 微型数据（10-20 个数据点）→ 完整模拟（500 个数据点）
- 先 MD 公式，再 Code 实现，再 scipy 验证
- 📊 步骤 N: 格式打印
- 可视化：英文标签，中文 print 解释
- 结尾：📌 核心概念回顾 + ❌ 常见误区（4-5条）

完成后运行 kernel 确认所有 cell 无报错。
```

---

## S2: Ch3 描述统计进阶

```
为《基础统计学(第14版)》第 3-2 和 3-3 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 3-2 离散程度的度量指标：约 p.74-86
- 3-3 相对位置的度量与箱形图：约 p.87-98

通读后梳理：全距、方差、标准差公式；z分数、百分位数、四分位数、箱形图。

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/3.2-dispersion-tutorial.ipynb

主题：离散程度的度量指标

教学目标（5条）：
1. 理解全距、方差、标准差的定义和计算公式
2. 掌握总体方差 ($\sigma^2$) vs 样本方差 ($s^2$) 的区别（分母 n vs n-1）
3. 手算 10 个数据点的方差和标准差
4. 用 scipy 验证，扩展到 500 个数据点
5. 理解范围经验法则和切比雪夫定理的应用

参考原书要点：
- 全距 = 最大值 - 最小值
- 方差公式：$s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1}$
- 标准差公式：$s = \sqrt{s^2}$
- 范围经验法则：约 68% 数据在 $\bar{x} \pm 1s$ 内，95% 在 $\bar{x} \pm 2s$ 内
- 切比雪夫定理：至少 $1 - 1/k^2$ 的数据在 $\bar{x} \pm ks$ 内

### Notebook 2: statistics_tutorial/3.3-relative-position-tutorial.ipynb

主题：z分数、百分位数与箱形图

教学目标（5条）：
1. 理解 z 分数的定义：$z = \frac{x - \bar{x}}{s}$，衡量数据点的相对位置
2. 掌握百分位数和四分位数的计算方法
3. 学会构建五数概括法和箱形图
4. 用箱形图识别异常值（IQR 方法）
5. 比较不同数据集的分布特征

参考原书要点：
- z 分数用于比较不同量纲的数据
- 百分位数的计算：$P_k$ 的位置 = $\frac{k(n+1)}{100}$
- 四分位数：$Q_1 = P_{25}$, $Q_2 = P_{50}$, $Q_3 = P_{75}$
- IQR = $Q_3 - Q_1$
- 异常值判断：低于 $Q_1 - 1.5 \times IQR$ 或高于 $Q_3 + 1.5 \times IQR$

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S3: Ch4 概率论基础

```
为《基础统计学(第14版)》第 4-1、4-2 和 4-3 节编写 3 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 4-1 概率：约 p.104-113
- 4-2 加法原理和乘法原理：约 p.114-125
- 4-3 对立事件、条件概率以及贝叶斯定理：约 p.126-137

通读后梳理：概率定义、加法规则、乘法规则、条件概率、贝叶斯定理。

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/4.1-probability-basics-tutorial.ipynb

主题：概率基本概念

教学目标（5条）：
1. 理解概率的三种定义：相对频数法、经典计算法、主观估计法
2. 掌握样本空间、事件、简单事件的概念
3. 用模拟实验验证概率（掷骰子、抽牌）
4. 理解概率的范围：$0 \leq P(A) \leq 1$
5. 区分实际发生比与赔率

参考原书要点：
- 概率的定义：$P(A) = \frac{A发生的次数}{总次数}$
- 简单事件和样本空间
- 相对频数法：大量重复实验
- 经典计算法：等可能事件
- 主观估计法：个人判断

### Notebook 2: statistics_tutorial/4.2-addition-multiplication-tutorial.ipynb

主题：加法原理和乘法原理

教学目标（5条）：
1. 理解互斥事件和非互斥事件的区别
2. 掌握加法规则：$P(A \cup B) = P(A) + P(B) - P(A \cap B)$
3. 理解独立事件和非独立事件
4. 掌握乘法规则：$P(A \cap B) = P(A) \times P(B|A)$
5. 用模拟实验验证加法和乘法规则

### Notebook 3: statistics_tutorial/4.3-conditional-bayes-tutorial.ipynb

主题：条件概率与贝叶斯定理

教学目标（5条）：
1. 理解条件概率的定义：$P(A|B) = \frac{P(A \cap B)}{P(B)}$
2. 掌握乘法原理的条件概率形式
3. 理解全概率公式和贝叶斯定理
4. 手算贝叶斯定理的医学检验问题
5. 用模拟验证贝叶斯定理的结果

参考原书要点：
- 条件概率的定义和计算
- 贝叶斯定理：$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$
- 医学检验结果的解读（假阳性、假阴性）

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S4: Ch4 计数法则 + Ch5 离散分布

```
为《基础统计学(第14版)》第 4-4、5-1 和 5-2 节编写 3 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 4-4 计数法则：约 p.138-148
- 5-1 概率分布：约 p.151-162
- 5-2 二项分布：约 p.163-175

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/4.4-counting-rules-tutorial.ipynb

主题：计数法则

教学目标（5条）：
1. 掌握乘法计数法则
2. 理解阶乘的定义和计算
3. 掌握排列和组合的区别和公式
4. 手算彩票中奖概率
5. 用 scipy.special.comb/perm 验证

### Notebook 2: statistics_tutorial/5.1-probability-distribution-tutorial.ipynb

主题：概率分布与期望值

教学目标（5条）：
1. 理解离散随机变量和概率分布
2. 掌握概率分布表的构建
3. 计算概率分布的均值、方差和标准差
4. 理解期望值的概念和计算
5. 用范围经验法则确定显著值

### Notebook 3: statistics_tutorial/5.2-binomial-distribution-tutorial.ipynb

主题：二项分布

教学目标（5条）：
1. 理解二项分布的四个条件
2. 掌握二项概率公式：$P(x) = C(n,x) \times p^x \times (1-p)^{n-x}$
3. 用 scipy.stats.binom 计算概率
4. 计算二项分布的均值和标准差
5. 用参数判断显著性

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S5: Ch5 泊松分布 + Ch6 正态分布基础

```
为《基础统计学(第14版)》第 5-3、6-1 和 6-2 节编写 3 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 5-3 泊松分布：约 p.176-180
- 6-1 标准正态分布：约 p.183-195
- 6-2 正态分布的实际应用：约 p.196-201

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/5.3-poisson-distribution-tutorial.ipynb

主题：泊松分布

教学目标（5条）：
1. 理解泊松分布的适用条件（稀有事件）
2. 掌握泊松概率公式：$P(x) = \frac{\mu^x \times e^{-\mu}}{x!}$
3. 用 scipy.stats.poisson 计算概率
4. 理解泊松分布与二项分布的关系
5. 应用泊松分布求解实际问题（飓风发生、缺陷率）

### Notebook 2: statistics_tutorial/6.1-standard-normal-tutorial.ipynb

主题：标准正态分布

教学目标（5条）：
1. 理解标准正态分布的特征（$\mu=0, \sigma=1$）
2. 掌握 z 分数的计算和含义
3. 学会用 scipy.stats.norm 计算面积（概率）
4. 掌握求给定面积对应的 z 值（临界值）
5. 理解对称性和面积的关系

### Notebook 3: statistics_tutorial/6.2-normal-application-tutorial.ipynb

主题：正态分布的实际应用

教学目标（5条）：
1. 将实际问题转化为正态分布问题
2. 掌握非标准正态分布的标准化方法
3. 计满足条件的百分比或人数
4. 确定满足特定概率的临界值
5. 用正态分布进行质量控制判断

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S6: Ch6 抽样分布 + 中心极限定理 + 正态性检验

```
为《基础统计学(第14版)》第 6-3、6-4 和 6-5 节编写 3 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 6-3 抽样分布和估计量：约 p.202-210
- 6-4 中心极限定理：约 p.211-218
- 6-5 正态性检验：约 p.219-225

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/6.3-sampling-distribution-tutorial.ipynb

主题：抽样分布和估计量

教学目标（5条）：
1. 理解抽样分布的概念（样本统计量的分布）
2. 掌握样本比例、样本均值、样本方差的抽样分布
3. 理解标准误的定义和计算
4. 用模拟实验展示抽样分布的形态
5. 理解估计量的性质（无偏性、一致性、有效性）

### Notebook 2: statistics_tutorial/6.4-clt-tutorial.ipynb

主题：中心极限定理

教学目标（5条）：
1. 理解中心极限定理的表述
2. 用模拟实验验证：不同总体分布下样本均值趋近正态
3. 理解样本量对抽样分布形态的影响
4. 掌握标准误公式：$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$
5. 理解中心极限定理在实际应用中的重要性

### Notebook 3: statistics_tutorial/6.5-normality-test-tutorial.ipynb

主题：正态性检验

教学目标（5条）：
1. 掌握 Shapiro-Wilk 检验的使用
2. 学会用 QQ 图评估正态性
3. 理解偏度和峰度的含义
4. 综合多种方法判断数据是否正态
5. 理解正态性检验对后续统计推断的影响

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S7: Ch7 参数估计

```
为《基础统计学(第14版)》第 7-1、7-2、7-3 和 7-4 节编写 4 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 7-1 总体比例的估计：约 p.227-238
- 7-2 总体均值的估计：约 p.239-248
- 7-3 总体标准差或方差的估计：约 p.249-253
- 7-4 自助法：约 p.254-260

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/7.1-proportion-estimation-tutorial.ipynb

主题：总体比例的估计

教学目标（5条）：
1. 理解点估计和区间估计的区别
2. 掌握比例的置信区间公式：$\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$
3. 理解误差范围的含义和计算
4. 掌握样本量的确定方法
5. 用模拟验证置信区间的覆盖概率

### Notebook 2: statistics_tutorial/7.2-mean-estimation-tutorial.ipynb

主题：总体均值的估计

教学目标（5条）：
1. 理解 t 分布的特征和与正态分布的关系
2. 掌握均值的置信区间公式：$\bar{x} \pm t_{\alpha/2} \frac{s}{\sqrt{n}}$
3. 理解自由度的概念
4. 用 scipy.stats.t 计算临界值和置信区间
5. 理解样本量与置信区间宽度的关系

### Notebook 3: statistics_tutorial/7.3-variance-estimation-tutorial.ipynb

主题：总体方差的估计

教学目标（5条）：
1. 理解卡方分布的特征
2. 掌握方差的置信区间公式
3. 用 scipy.stats.chi2 计算临界值
4. 构建标准差的置信区间
5. 理解方差估计的特殊性

### Notebook 4: statistics_tutorial/7.4-bootstrap-tutorial.ipynb

主题：自助法

教学目标（5条）：
1. 理解自助法的基本原理（重抽样）
2. 掌握自助法置信区间的构建步骤
3. 用 Python 实现自助法
4. 对比自助法与传统方法的结果
5. 理解自助法的优势和适用场景

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S8: Ch8 假设检验

```
为《基础统计学(第14版)》第 8-1、8-2、8-3 和 8-4 节编写 4 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 8-1 假设检验的基础：约 p.261-275
- 8-2 总体比例的假设检验：约 p.276-282
- 8-3 总体均值的假设检验：约 p.283-295
- 8-4 总体标准差或方差的假设检验：约 p.296-300

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/8.1-hypothesis-testing-basics-tutorial.ipynb

主题：假设检验基础

教学目标（5条）：
1. 理解零假设和备择假设的设定
2. 掌握第一类错误（α）和第二类错误（β）
3. 理解 p 值的含义和计算
4. 掌握统计功效的概念和计算
5. 理解显著性水平的选择（0.05, 0.01）

### Notebook 2: statistics_tutorial/8.2-proportion-test-tutorial.ipynb

主题：总体比例的假设检验

教学目标（5条）：
1. 掌握比例检验的假设设定
2. 理解正态近似法的条件
3. 计算检验统计量和 p 值
4. 用 scipy 进行比例检验
5. 理解精确法与近似法的区别

### Notebook 3: statistics_tutorial/8.3-mean-test-tutorial.ipynb

主题：总体均值的假设检验

教学目标（5条）：
1. 掌握单样本 t 检验的假设设定
2. 理解 p 值法、临界值法和置信区间法
3. 手算 t 统计量并查表
4. 用 scipy.stats.ttest_1samp 验证
5. 理解双侧检验和单侧检验的区别

### Notebook 4: statistics_tutorial/8.4-variance-test-tutorial.ipynb

主题：总体方差的假设检验

教学目标（5条）：
1. 掌握卡方检验的假设设定
2. 理解卡方检验统计量的计算
3. 用 scipy.stats.chi2 进行方差检验
4. 构建置信区间并判断显著性
5. 理解方差检验的实际应用

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S9: Ch9 两样本推断 + Ch10 相关与回归

```
为《基础统计学(第14版)》第 9-2、9-3、10-1 和 10-2 节编写 4 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 9-2 两个总体均值（独立样本）：约 p.308-315
- 9-3 配对样本：约 p.316-322
- 10-1 相关分析：约 p.328-340
- 10-2 线性回归：约 p.341-352

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/9.2-two-sample-mean-tutorial.ipynb

主题：两个总体均值（独立样本）

教学目标（5条）：
1. 理解独立两样本 t 检验的条件
2. 掌握合并方差和分开方差的方法
3. 手算 t 统计量
4. 用 scipy.stats.ttest_ind 验证
5. 理解方差齐性检验的重要性

### Notebook 2: statistics_tutorial/9.3-paired-sample-tutorial.ipynb

主题：配对样本

教学目标（5条）：
1. 理解配对样本和独立样本的区别
2. 掌握配对 t 检验的步骤
3. 计算差值的均值和标准差
4. 用 scipy.stats.ttest_rel 验证
5. 理解配对设计的优势

### Notebook 3: statistics_tutorial/10.1-correlation-tutorial.ipynb

主题：相关分析

教学目标（5条）：
1. 理解 Pearson 相关系数 r 的含义
2. 掌握 r 的计算公式
3. 理解相关性的假设检验
4. 区分相关性和因果性
5. 识别伪相关和可解释变异

### Notebook 4: statistics_tutorial/10.2-linear-regression-tutorial.ipynb

主题：线性回归

教学目标（5条）：
1. 理解最小二乘法的原理
2. 掌握回归方程的计算
3. 理解残差和残差分析
4. 识别强影响点
5. 评估回归模型的拟合优度

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S10: Ch10-13 进阶方法

```
为《基础统计学(第14版)》第 10-4、11-1、11-2、12-1、13-4 和 13-5 节编写 6 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber + pytesseract OCR 提取原书内容。
- 10-4 多元线性回归：约 p.353-362
- 11-1 拟合优度检验：约 p.365-370
- 11-2 列联表：约 p.371-382
- 12-1 单因素方差分析：约 p.385-398
- 13-4 威尔科克森秩和检验：约 p.418-422
- 13-5 Kruskal-Wallis 检验：约 p.423-426

## 第二步：参考已有教程风格

读取 .claude/skills/stats-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: statistics_tutorial/10.4-multiple-regression-tutorial.ipynb

主题：多元线性回归

教学目标（5条）：
1. 理解多元回归方程的结构
2. 掌握虚拟变量的使用
3. 理解 R² vs 调整 R² 的区别
4. 识别多重共线性问题
5. 用 statsmodels 进行多元回归分析

### Notebook 2: statistics_tutorial/11.1-goodness-of-fit-tutorial.ipynb

主题：拟合优度检验

教学目标（5条）：
1. 理解卡方拟合优度检验的原理
2. 掌握观测频数和期望频数的计算
3. 手算卡方统计量
4. 用 scipy.stats.chisquare 验证
5. 了解本福特定律的应用

### Notebook 3: statistics_tutorial/11.2-contingency-table-tutorial.ipynb

主题：列联表检验

教学目标（5条）：
1. 理解列联表的结构
2. 掌握独立性检验的步骤
3. 理解同质性检验和费希尔精确检验
4. 用 scipy.stats.chi2_contingency 进行检验
5. 解读列联表检验的结果

### Notebook 4: statistics_tutorial/12.1-anova-one-way-tutorial.ipynb

主题：单因素方差分析

教学目标（5条）：
1. 理解方差分析的目的和条件
2. 掌握 F 检验的原理（组间/组内变异）
3. 手算 F 统计量
4. 用 scipy.stats.f_oneway 验证
5. 理解事后比较（Bonferroni 校正）

### Notebook 5: statistics_tutorial/13.4-wilcoxon-rank-sum-tutorial.ipynb

主题：威尔科克森秩和检验

教学目标（5条）：
1. 理解非参数检验的优势和适用场景
2. 掌握秩和检验的步骤
3. 手算秩次和检验统计量
4. 用 scipy.stats.ranksums 验证
5. 对比秩和检验与 t 检验的结果

### Notebook 6: statistics_tutorial/13.5-kruskal-wallis-tutorial.ipynb

主题：Kruskal-Wallis 检验

教学目标（5条）：
1. 理解 Kruskal-Wallis 检验是单因素 ANOVA 的非参数替代
2. 掌握检验的假设设定和计算步骤
3. 用 scipy.stats.kruskal 进行检验
4. 理解事后比较方法
5. 对比 Kruskal-Wallis 与 ANOVA 的结果

额外规范：
- 非参数检验教程必须包含与参数检验的对比
- 结尾 ❌ 常见误区必须包含"在不满足参数检验条件时误用参数方法"

共同规范同 S1。完成后运行 kernel 确认无报错。
```
