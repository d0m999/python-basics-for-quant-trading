# 10 个 Session 直接可实施提示词（修订版）

> 基于 PDF 实际目录结构修订，2026-05-29
> 书籍路径：/Users/d0m999/Desktop/_rag/Factor investing.pdf
> 规范文件：.claude/skills/quant-notebook-tutorial.md

---

## 通用前置说明

每个 prompt 执行前，agent 必须：

1. **先读原书章节**：用 pdfplumber 提取对应页码的文本，理解章节的公式、逻辑、实证方法
2. **再读参考 notebook**：读取 quant_tutorial/ 下已有教程的风格
3. **最后编写教程**：严格遵循 quant-notebook-tutorial.md 规范

```python
# 通用读取模板（每个 prompt 开头执行）
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text = ""
for page in pdf.pages[START-1:END]:  # 页码从 0 开始
    text += page.get_text()
print(text[:6000])  # 先看结构
```

---

## S1: Ch3 规模因子 + 价值因子

```
为《因子投资：方法与实践》第 3.3 和 3.4 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

用 pdfplumber 提取原书第 3.3 节（约 p.117-121）和第 3.4 节（约 p.122-128）的文本内容。
书籍路径：/Users/d0m999/Desktop/_rag/Factor investing.pdf

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_33 = ""
for page in pdf.pages[116:121]:
    text_33 += page.get_text()
text_34 = ""
for page in pdf.pages[121:128]:
    text_34 += page.get_text()
print("=== 3.3 规模因子 ===")
print(text_33[:4000])
print("\n=== 3.4 价值因子 ===")
print(text_34[:4000])
```

通读后梳理：核心公式、分组方法、实证结论、A 股特殊性。

## 第二步：参考已有教程风格

读取 quant_tutorial/2.1-portfolio-sorts-tutorial.ipynb 了解风格。
读取 .claude/skills/quant-notebook-tutorial.md 了解规范。

## 第三步：编写教程

### Notebook 1: quant_tutorial/3.3-size-factor-tutorial.ipynb

主题：规模因子 (SMB)——小市值效应

教学目标（5条）：
1. 理解规模因子的定义：按市值分组，小市值组 - 大市值组 = SMB
2. 掌握 A 股中市值分组的具体操作（流通市值、对数处理）
3. 在微型数据集（10 只股票）上手算分组和 Spread
4. 扩展到 300 只股票 × 60 月，完成 T 检验和单调性检验
5. 理解 A 股小市值效应的历史表现和风险

参考原书要点：
- 市值因子的学术起源（Banz 1981）
- A 股中按流通市值分组的具体方法
- 等权 vs 市值加权的差异
- SMB 的 FMP 构建

### Notebook 2: quant_tutorial/3.4-value-factor-tutorial.ipynb

主题：价值因子 (HML)——价值溢价

教学目标（5条）：
1. 理解价值因子的定义：B/M 比（账面市值比）
2. 掌握 B/M 的计算方法和数据处理（滞后处理避免前视偏差）
3. 在微型数据集上手算 B/M 分组和 HML Spread
4. 扩展到完整规模，完成 Fama-MacBeth 回归和 IC 分析
5. 理解 A 股价值效应的时变特征

参考原书要点：
- B/M = 每股净资产 / 股价（使用上一年年报数据，滞后处理）
- 分组方法：按 B/M 从高到低分 5 组，HML = Q1(高B/M) - Q5(低B/M)
- 与 E/P、CF/P 等其他价值指标的比较

共同规范：
- 微型数据（10 只股票 × 1 月）→ 完整模拟（300 只 × 60 月）
- 先 MD 公式，再 Code 实现，再 scipy 验证
- 📊 步骤 N: 格式打印
- 可视化：英文标签，中文 print 解释
- 结尾：📌 核心概念回顾 + ❌ 常见误区（4-5条）

完成后运行 kernel 确认所有 cell 无报错。
```

---

## S2: Ch3 动量因子 + 换手率因子

```
为《因子投资：方法与实践》第 3.5 和 3.8 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_35 = ""
for page in pdf.pages[128:136]:  # 3.5 动量因子
    text_35 += page.get_text()
text_38 = ""
for page in pdf.pages[151:157]:  # 3.8 换手率因子
    text_38 += page.get_text()
print("=== 3.5 动量因子 ===")
print(text_35[:4000])
print("\n=== 3.8 换手率因子 ===")
print(text_38[:4000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.3-factor-exposure-returns-tutorial.ipynb 和 .claude/skills/quant-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: quant_tutorial/3.5-momentum-factor-tutorial.ipynb

主题：动量因子 (WML)——追涨杀跌的利润

教学目标：
1. 理解动量因子的定义：过去 12 个月累计收益率（跳过最近 1 个月）
2. 掌握 A 股动量因子的构建：formation period + holding period
3. 手算 10 只股票的动量值和分组
4. 扩展到完整规模，检验动量效应的显著性
5. 理解 A 股动量效应的特殊性（动量崩溃、反转效应）

参考原书要点：
- Jegadeesh and Titman (1993) 的经典动量策略
- 跳过最近 1 个月（避免短期反转污染）
- A 股动量效应的实证结果

### Notebook 2: quant_tutorial/3.8-turnover-factor-tutorial.ipynb

主题：换手率因子——A 股特有的因子

教学目标：
1. 理解换手率因子的定义：月均换手率
2. 掌握 A 股换手率因子的构建方法
3. 手算分组检验过程
4. 扩展到完整规模，检验低换手率溢价
5. 理解 A 股低换手率溢价的行为金融学解释

参考原书要点：
- 换手率 = 月成交量 / 流通股本
- A 股中低换手率股票获得更高收益（流动性溢价）
- 与国际市场的差异

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S3: Ch3 盈利因子 + 投资因子

```
为《因子投资：方法与实践》第 3.6 和 3.7 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_36 = ""
for page in pdf.pages[136:143]:  # 3.6 盈利因子
    text_36 += page.get_text()
text_37 = ""
for page in pdf.pages[143:151]:  # 3.7 投资因子
    text_37 += page.get_text()
print("=== 3.6 盈利因子 ===")
print(text_36[:4000])
print("\n=== 3.7 投资因子 ===")
print(text_37[:4000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.4-anomaly-tests-tutorial.ipynb 和 .claude/skills/quant-notebook-tutorial.md

## 第三步：编写教程

### Notebook 1: quant_tutorial/3.6-profitability-factor-tutorial.ipynb

主题：盈利因子 (RMW)——高盈利溢价

教学目标：
1. 理解盈利因子的定义：ROE/ROA/毛利率等盈利指标
2. 掌握 Fama-French 五因子中 RMW 的构建方法
3. 手算盈利分组和 Spread
4. 扩展到完整规模，检验高盈利组合的超额收益
5. 理解盈利因子与价值因子的关系

### Notebook 2: quant_tutorial/3.7-investment-factor-tutorial.ipynb

主题：投资因子 (CMA)——保守投资溢价

教学目标：
1. 理解投资因子的定义：总资产增长率
2. 掌握 CMA（Conservative Minus Aggressive）的构建
3. 手算投资分组和 Spread
4. 扩展到完整规模，检验保守投资策略的表现
5. 理解投资因子的经济学含义（资产增长 anomaly）

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S4: Ch4 多因子模型综述 + 模型比较

```
为《因子投资：方法与实践》第 4.1 和 4.3 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_41 = ""
for page in pdf.pages[158:174]:  # 4.1 主流多因子模型综述
    text_41 += page.get_text()
text_43 = ""
for page in pdf.pages[176:189]:  # 4.3 多因子模型比较
    text_43 += page.get_text()
print("=== 4.1 主流多因子模型综述 ===")
print(text_41[:5000])
print("\n=== 4.3 多因子模型比较 ===")
print(text_43[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.5-model-comparison-tutorial.ipynb（GRS 检验教程）

## 第三步：编写教程

### Notebook 1: quant_tutorial/4.1-multi-factor-models-overview-tutorial.ipynb

主题：主流多因子模型综述

教学目标：
1. 理解多因子模型的统一框架：r_i = α_i + Σ β_ik × f_k + ε_i
2. 掌握 7 个主流模型：CAPM、FF3、Carhart4、FF5、q-factor、中国版三因子、DHS
3. 对比各模型的因子组成和经济学含义
4. 用模拟数据构建各模型的因子收益率
5. 可视化各模型因子的相关性矩阵

### Notebook 2: quant_tutorial/4.3-model-comparison-tutorial.ipynb

主题：多因子模型比较——来自 A 股的例子

教学目标：
1. 理解 GRS 检验的原理：联合检验所有 α = 0
2. 掌握 GRS 统计量的计算：手算 → scipy 验证
3. 使用平均 |α| 作为模型比较的辅助指标
4. 在 A 股数据上比较 7 个模型的解释能力
5. 构建模型比较矩阵（GRS、|α|、R²）

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S5: Ch5 估值异象 + 基本面反转

```
为《因子投资：方法与实践》第 5.1 和 5.2 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_51 = ""
for page in pdf.pages[193:204]:  # 5.1 估值高低中的异象
    text_51 += page.get_text()
text_52 = ""
for page in pdf.pages[204:213]:  # 5.2 基本面锚定反转
    text_52 += page.get_text()
print("=== 5.1 估值异象 ===")
print(text_51[:4000])
print("\n=== 5.2 基本面反转 ===")
print(text_52[:4000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.4-anomaly-tests-tutorial.ipynb

## 第三步：编写教程

### Notebook 1: quant_tutorial/5.1-valuation-anomaly-tutorial.ipynb

主题：估值高低中的异象

教学目标：
1. 理解估值异象的核心：估值指标（E/P, B/M, CF/P）能预测未来收益
2. 掌握异象检验的完整流程：分组 → 多空组合 → 控制已知因子 → 检验 α
3. 手算 E/P 分组和 Fama-MacBeth 回归
4. 扩展到完整规模，检验估值异象在 A 股的显著性
5. 区分真异象（显著 α）和伪异象（被已知因子解释）

### Notebook 2: quant_tutorial/5.2-fundamental-reversal-tutorial.ipynb

主题：基本面锚定反转

教学目标：
1. 理解基本面锚定反转的定义：基于估值偏离的反转策略
2. 掌握短期反转（1 个月）和长期反转（3-5 年）的区别
3. 手算反转信号的构建
4. 扩展到完整规模，检验反转效应的显著性
5. 理解反转效应与动量效应的互补关系

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S6: Ch5 特质波动率

```
为《因子投资：方法与实践》第 5.3 节编写 1 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_53 = ""
for page in pdf.pages[213:223]:  # 5.3 特质性波动率
    text_53 += page.get_text()
print("=== 5.3 特质性波动率 ===")
print(text_53[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.2-regression-tests-tutorial.ipynb（回归方法）

## 第三步：编写教程

### Notebook: quant_tutorial/5.3-idiosyncratic-volatility-tutorial.ipynb

主题：特质性波动率异象 (IVOL Anomaly)

教学目标：
1. 理解特质波动率 (IVOL) 的定义：CAPM/FF3 回归残差的标准差
2. 掌握 IVOL 的计算方法：时序回归 → 残差 → 标准差
3. 手算 10 只股票的 IVOL
4. 扩展到完整规模，检验 IVOL 异象（低 IVOL 组合表现更好）
5. 理解 IVOL 异象的行为金融学解释（lottery demand）

参考原书要点：
- Ang et al. (2006) 的经典发现
- IVOL 与横截面收益的负相关关系
- A 股 IVOL 异象的实证结果
- 与 lottery demand 和套利限制的关系

规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S7: Ch7 收益率模型 + 风险模型

```
为《因子投资：方法与实践》第 7.1 和 7.2 节编写 2 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_71 = ""
for page in pdf.pages[292:305]:  # 7.1 收益率模型
    text_71 += page.get_text()
text_72 = ""
for page in pdf.pages[305:316]:  # 7.2 风险模型
    text_72 += page.get_text()
print("=== 7.1 收益率模型 ===")
print(text_71[:5000])
print("\n=== 7.2 风险模型 ===")
print(text_72[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.3-factor-exposure-returns-tutorial.ipynb

## 第三步：编写教程

### Notebook 1: quant_tutorial/7.1-alpha-model-tutorial.ipynb

主题：收益率模型——获取"阿尔法"

教学目标：
1. 理解 α 模型的核心：预测资产的超额收益率
2. 掌握多因子模型作为 α 模型的使用方式
3. 因子暴露估计：时间序列回归 vs 截面特征
4. 预期收益率的计算和评估（IC、ICIR）
5. α 模型与风险模型的配合使用

### Notebook 2: quant_tutorial/7.2-risk-model-barra-tutorial.ipynb

主题：风险模型——以 Barra 为例

教学目标：
1. 理解 Barra 风险模型的整体架构：因子暴露 B、因子协方差 Σ_F、特质方差 D
2. 掌握 Barra 因子体系（国家因子 + 行业因子 + 风格因子）
3. 构建简化 Barra 模型：5 行业 + 3 风格因子
4. 用矩阵运算计算组合风险和个股风险
5. 可视化因子暴露热力图和风险分解

共同规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S8: Ch7 组合优化

```
为《因子投资：方法与实践》第 7.3 节编写 1 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_73 = ""
for page in pdf.pages[316:327]:  # 7.3 投资组合优化
    text_73 += page.get_text()
print("=== 7.3 投资组合优化 ===")
print(text_73[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.1-portfolio-sorts-tutorial.ipynb

## 第三步：编写教程

### Notebook: quant_tutorial/7.3-portfolio-optimization-tutorial.ipynb

主题：投资组合优化

教学目标：
1. 理解因子投资组合优化的目标函数
2. 掌握约束条件的设置：权重和、行业偏离、因子暴露、换手率
3. 手算 5 只股票 2 因子的简化优化问题（KKT 条件）
4. 使用 scipy.optimize 求解并验证
5. 对比等权组合 vs 优化组合的绩效差异

参考原书要点：
- 目标函数：max w'Bf - λ/2 × w'BΣ_F B'w
- 约束条件的实际含义
- 换手率惩罚的加入
- 优化结果的经济直觉

规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S9: Ch7 Smart Beta

```
为《因子投资：方法与实践》第 7.4 节编写 1 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_74 = ""
for page in pdf.pages[327:351]:  # 7.4 Smart Beta
    text_74 += page.get_text()
print("=== 7.4 Smart Beta ===")
print(text_74[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.1-portfolio-sorts-tutorial.ipynb

## 第三步：编写教程

### Notebook: quant_tutorial/7.4-smart-beta-tutorial.ipynb

主题：Smart Beta——因子投资的捷径

教学目标：
1. 理解 Smart Beta 的定义：介于纯被动和纯主动之间的因子投资
2. 掌握常见 Smart Beta 策略：等权、最小方差、风险平价、基本面加权、高股息
3. 实现各策略的权重计算
4. 对比不同策略的因子暴露、收益和风险特征
5. 理解 A 股 Smart Beta ETF 产品生态

参考原书要点：
- Smart Beta 的兴起和分类
- 各策略的优缺点对比
- 因子投资 vs Smart Beta 的关系
- A 股市场的 Smart Beta 实践

规范同 S1。完成后运行 kernel 确认无报错。
```

---

## S10: Ch6 机器学习与因子投资

```
为《因子投资：方法与实践》第 6.8 节编写 1 个 Jupyter Notebook 教程。

## 第一步：阅读原书

```python
import pdfplumber
pdf = pdfplumber.open("/Users/d0m999/Desktop/_rag/Factor investing.pdf")
text_68 = ""
for page in pdf.pages[280:290]:  # 6.8 机器学习与因子投资
    text_68 += page.get_text()
print("=== 6.8 机器学习与因子投资 ===")
print(text_68[:5000])
```

## 第二步：参考已有教程

读取 quant_tutorial/2.5-model-comparison-tutorial.ipynb

## 第三步：编写教程

### Notebook: quant_tutorial/6.8-ml-factor-investing-tutorial.ipynb

主题：机器学习与因子投资

额外依赖：sklearn（Lasso, Ridge, RandomForestRegressor, GradientBoostingRegressor）

教学目标：
1. 理解机器学习在因子投资中的三个应用：特征选择、非线性建模、预测
2. 掌握正则化方法（LASSO/Ridge/ElasticNet）进行因子选择
3. 使用树模型（RF/GBDT）捕捉因子的非线性效应
4. 理解金融领域交叉验证的特殊性（Purged K-Fold）
5. 对比线性模型 vs 树模型的预测能力和 IC

参考原书要点：
- 机器学习对因子研究的贡献
- 过拟合风险和防范措施
- 特征重要性与可解释性
- 样本外预测的评估

规范同 S1。额外注意：
- sklearn import 放在 Cell 2 的 import 区域
- 时序分割不能用标准 K-Fold，必须用 Purged/Expanding window
- 结尾 ❌ 常见误区必须包含"用未来数据训练"的前视偏差

完成后运行 kernel 确认无报错。
```
