---
trigger: "notebook" OR "tutorial" OR "教程" OR "统计学" OR "statistics" OR "假设检验" OR "置信区间" OR "概率" OR "基础统计学"
description: Concrete notebook construction workflow for statistics tutorial notebooks. Covers cell structure, code patterns, visualization conventions, and quality checklist based on 《基础统计学(第14版)》.
alwaysApply: false
---

# Statistics Tutorial Notebook Construction Guide

This skill defines the **concrete notebook construction workflow** for statistics tutorials based on 《基础统计学(第14版)》 (Triola). Cell organization, code idioms, markdown formatting, and visualization patterns.

---

## 1. Notebook Skeleton

Every tutorial notebook follows this standard cell sequence:

```
Cell 0  [MD]   Title + 教学目标 + 参考书
Cell 1  [MD]   场景设定 / 动机 (🎯 问题)
Cell 2  [Code] Imports + 环境配置
Cell 3+ [MD]   Section headers with step-by-step content
        [Code] Micro-example (10-25 data points, hand-calc visible)
        [Code] Scaled example (100-500 data points)
        [Code] scipy / statsmodels verification
        [Code] Visualization cells
Cell N-2 [MD]  📌 核心概念回顾
Cell N-1 [MD]  ❌ 常见误区
```

### Title Cell Template

```markdown
# [Topic] 完整教程：从 [Simple] 到 [Complex]

## 📚 教学目标
1. 理解 [concept A] 的完整计算步骤
2. 掌握 [concept B] 的概念
3. 可视化 [concept C]
4. 理解为什么 [key insight]
5. [第5个目标]

**参考书**：《基础统计学(第14版)》（Triola）第 X 章
**教学策略**：先用极小数据集让你"看见"每一步计算，再扩展到真实规模
```

### Progressive Scaling Pattern

Notebooks must follow micro → macro scaling:

| Stage | Data Size | Purpose |
|-------|-----------|---------|
| Micro example | 10-25 items | Hand-calc every step, build intuition |
| Medium scale | 50-100 items | Show patterns emerging |
| Full simulation | 200-500 items | Statistical inference |

---

## 2. Markdown Cell Conventions

### Section Headers

Use `## N.` for major sections (numbered sequentially):

```markdown
## 1. 场景设定：单样本 T 检验
## 2. 生成样本数据
## 3. T 检验完整计算步骤
## 4. 使用 scipy 验证计算结果
...
## 10. 核心概念回顾
## 11. 常见误区提醒
```

### Sub-headers with Emoji

Use `### emoji topic` for sub-sections. Standard emoji vocabulary:

| Emoji | Usage |
|-------|-------|
| 📐 | Formulas, math derivation, calculation steps |
| 📊 | Data display, results, statistics |
| 💡 | Key insight, interpretation, "why" explanation |
| 📌 | Core concept review (回顾 section) |
| 🎯 | Problem statement, goal, conclusion |
| 📖 | Book citation, textbook reference |
| 🔗 | Relationships between concepts |
| 📝 | Summary tables |
| 🔬 | scipy/library verification |

### LaTeX Patterns

Inline math: `$\bar{x}$`, `$\mu_0$`, `$\sigma$`

Display math for key formulas:

```markdown
$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$
```

Always define variables after display math:

```markdown
其中：
- $\bar{x}$ = 样本均值
- $\mu_0$ = 假设的总体均值
- $s$ = 样本标准差
- $n$ = 样本量
```

### 📌 核心概念回顾 Format

Each concept uses this structure:

```markdown
### 📌 [Concept Name] ([English Name])
- **定义**: [one-line definition]
- **公式**: $[formula]$
- **含义/意义**: [practical interpretation]
- **判断标准**: [threshold or rule of thumb]
```

End with a `### 🔗 完整流程` showing the workflow as ASCII pipeline:

```markdown
### 🔗 完整流程
\```
步骤A → 步骤B → 步骤C → 步骤D
    ↓         ↓         ↓         ↓
  说明      说明       说明      说明
\```
```

And a `### 📝 检验指标汇总` comparison table.

### ❌ 常见误区 Format

```markdown
### ❌ 误区 N: [Misconception statement]
**✓ 正确理解**: [Correct understanding]
```

Or the compact form for review sections:

```markdown
#### 误区 N: [Misconception]
**✓ 正确做法**: [Correct approach]
```

Include 4-5 misconceptions per notebook. Focus on conceptual errors, not coding bugs.

### Book Citation Format

```markdown
### 📖 书中的定义
> [Exact quote from textbook in Chinese]

### 📖 书中要点
> [Paraphrased key point from textbook]
```

### Comparison Tables

Use markdown tables for contrasting concepts:

```markdown
| 特性 | 方法A | 方法B |
|------|-------|-------|
| 优点 | ✅ ... | ✅ ... |
| 缺点 | ⚠️ ... | ⚠️ ... |
| 适用场景 | ... | ... |
```

---

## 3. Code Cell Conventions

### Imports Template (Always Cell 2)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from scipy import stats

# 设置中文字体和样式
_cn_fonts = [f.name for f in fm.fontManager.ttflist if any(kw in f.name for kw in ['Hei', 'Song', 'PingFang', 'Arial Unicode', 'Noto Sans CJK', 'SimHei', 'Microsoft YaHei'])]
plt.rcParams['font.sans-serif'] = _cn_fonts[:3] + ['DejaVu Sans'] if _cn_fonts else ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")

np.random.seed(42)
print("✅ 库导入完成")
```

### Code Section Headers

Use decorated comments for major code sections:

```python
# ========== 步骤 N: [Description] ==========
```

### Step-by-Step Print Formatting

Every computation step prints its work with this pattern:

```python
print(f"\n📊 步骤 N: [Step Name]")
print(f"  [Variable Name] = {value:.4f}")
print(f"  计算公式: [formula in text]")
print(f"  实际计算: [substituted values] = {result:.4f}")
print(f"  \n💡 [Interpretation of result]")
```

Key formatting rules:
- Use `📊 步骤 N:` prefix for each computation step
- Show formula symbolically, then with substituted values
- End each step with `💡` interpretation
- Use 2-space indent for details under a step
- Use `.4f` for intermediate values, `.6f` for p-values
- Use `.2f` for display/summary values

### scipy Verification Pattern

After hand-calculating any statistic, always verify with scipy:

```python
# ========== 用 scipy 验证 ==========
t_scipy, p_scipy = stats.ttest_1samp(sample, hypothesized_mean)

print("🔬 scipy.stats.ttest_1samp 验证:")
print(f"  手算 T 统计量 = {t_manual:.6f}")
print(f"  scipy T 统计量 = {t_scipy:.6f}")
print(f"  手算 P 值     = {p_manual:.6f}")
print(f"  scipy P 值    = {p_scipy:.6f}")
print(f"\n  ✅ 验证通过！")
```

### Data Simulation (DGP) Pattern

When generating synthetic data, make the data-generating process explicit:

```python
# --- 数据生成过程 (DGP) ---
# 变量1: [distribution description]
data_var1 = np.random.normal(mean, std, n)

# 变量2: [distribution description]
data_var2 = np.random.uniform(low, high, n)
```

Always document:
1. What distribution each variable follows
2. The parameters of the distribution
3. The sample size

### Print Result Summary Pattern

For final summary reports:

```python
print("=" * 60)
print("📋 [Report Title]")
print("=" * 60)
print(f"\n🎯 研究问题:")
print(f"   [Question]")
print(f"\n📊 数据概况:")
print(f"   样本量: {n}")
# ... key statistics ...
print(f"\n🧮 统计检验:")
# ... test results ...
print(f"\n🎯 结论:")
if is_significant:
    print(f"  ✓ [Conclusion]")
else:
    print(f"  ✗ [Conclusion]")
print("\n" + "=" * 60)
```

---

## 4. Visualization Conventions

### Language Rule

- **Plot labels, titles, legends**: English
- **Print explanations below plots**: Chinese

```python
ax.set_xlabel('T Value', fontsize=12)          # English
ax.set_ylabel('Probability Density', fontsize=12)  # English
ax.set_title('T Distribution and T Value Position', fontsize=14, fontweight='bold')  # English
# ...
plt.show()

print(f"\n💡 图解说明：")  # Chinese explanation after plt.show()
print(f"  图1：...")
```

### Color Scheme

| Color | Hex | Usage |
|-------|-----|-------|
| Green | `#2ecc71` | Positive values, "good", acceptance region |
| Red | `#e74c3c` | Negative values, rejection region |
| Blue | `steelblue` | Neutral distributions, histograms |
| Orange | `#e67e22` | Warning, secondary emphasis |

For distribution plots with shaded regions:

```python
# Shade rejection region
ax.fill_between(x_reject, 0, y_reject, alpha=0.3, color='#e74c3c', label='Rejection Region')
# Shade acceptance region
ax.fill_between(x_accept, 0, y_accept, alpha=0.3, color='#2ecc71', label='Acceptance Region')
```

### Figure Sizes

| Layout | figsize |
|--------|---------|
| Single plot | `(10, 6)` or `(12, 5)` |
| 1×2 subplots | `(14, 5)` or `(16, 6)` |
| 1×3 subplots | `(18, 5)` |
| 2×2 subplots | `(16, 12)` |

### Standard Plot Elements

```python
sns.set_style("whitegrid")

# Font sizes
ax.set_xlabel('Label', fontsize=12)
ax.set_ylabel('Label', fontsize=12)
ax.set_title('Title', fontsize=14, fontweight='bold')  # always bold
ax.legend(fontsize=10)
ax.grid(alpha=0.3)  # or grid(axis='y', alpha=0.3) for bar charts
```

### Distribution Plot Pattern

```python
# Plot normal/t/chi-square distribution
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x)
ax.plot(x, y, 'b-', linewidth=2, label='Standard Normal')
ax.fill_between(x, 0, y, alpha=0.1, color='steelblue')

# Mark critical values
ax.axvline(x=-1.96, color='red', linestyle='--', alpha=0.7)
ax.axvline(x=1.96, color='red', linestyle='--', alpha=0.7)
```

### Histogram with Distribution Overlay

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins=20, density=True, alpha=0.6, color='steelblue', edgecolor='white')
# Overlay theoretical distribution
x = np.linspace(data.min(), data.max(), 100)
y = stats.norm.pdf(x, data.mean(), data.std())
ax.plot(x, y, 'r-', linewidth=2, label='Theoretical Normal')
```

### Box Plot Pattern

```python
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot([group1, group2, group3], labels=['Group 1', 'Group 2', 'Group 3'],
                patch_artist=True)
colors = ['#2ecc71', '#3498db', '#e74c3c']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set(alpha=0.7)
```

---

## 5. Pedagogical Flow

### Formula-Before-Code Rule

Always present the mathematical formula in a markdown cell **before** the code cell that implements it:

```
[MD Cell] ### 📐 计算公式
          $$formula$$
          其中：...

[Code Cell] # Implementation
            result = ...
```

### Hand-Calc → scipy Verification Chain

For every statistical test:
1. **Hand-calculate** step by step (步骤 1 through N)
2. **Verify** with scipy in a separate cell
3. **Print** both results side by side with `✅ 验证通过！`

### Progressive Complexity

| Phase | Data Size | Purpose |
|-------|-----------|---------|
| Micro | 10-25 items | See every calculation |
| Medium | 50-100 items | See patterns emerging |
| Full | 200-500 items | Statistical inference |

Scale transitions use explicit print statements:

```python
print(f"📊 模拟参数：")
print(f"  样本量: {n}")
print(f"  分布类型: Normal(μ={mu}, σ={sigma})")
```

### Section Flow for a Statistical Concept

```
1. 场景设定 (motivating question)
2. 公式推导 (LaTeX + variable definitions)
3. 微型数据手算 (10-25 items, print every step)
4. scipy 验证 (compare hand vs library)
5. 可视化 (English labels, Chinese print explanation)
6. 大样本扩展 (200-500 items, full test)
7. 总结报告 (formatted summary)
```

---

## 6. Statistics-Specific Patterns

### Confidence Interval Pattern

```python
# ========== 步骤 N: 构建置信区间 ==========
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
margin_of_error = t_critical * se
ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

print(f"📊 步骤 N: 构建 {confidence_level*100:.0f}% 置信区间")
print(f"  临界值 t_{{α/2}} = {t_critical:.4f}")
print(f"  误差范围 E = {margin_of_error:.4f}")
print(f"  置信区间 = ({ci_lower:.4f}, {ci_upper:.4f})")
```

### Hypothesis Test Pattern

```python
# ========== 步骤 N: 假设检验 ==========
print(f"\n📊 步骤 N: 假设检验")
print(f"  H₀: μ = {mu_0}")
print(f"  H₁: μ ≠ {mu_0}")  # or < or >

# Calculate test statistic
t_stat = (sample_mean - mu_0) / se
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

print(f"  检验统计量 t = {t_stat:.4f}")
print(f"  p 值 = {p_value:.6f}")
print(f"  显著性水平 α = {alpha}")

if p_value < alpha:
    print(f"\n  💡 结论: p < α，拒绝 H₀")
else:
    print(f"\n  💡 结论: p ≥ α，不拒绝 H₀")
```

### Verify with scipy

```python
# ========== 用 scipy 验证 ==========
t_scipy, p_scipy = stats.ttest_1samp(data, mu_0)

print("🔬 scipy.stats.ttest_1samp 验证:")
print(f"  手算 t = {t_stat:.6f}")
print(f"  scipy t = {t_scipy:.6f}")
print(f"  手算 p = {p_value:.6f}")
print(f"  scipy p = {p_scipy:.6f}")
print(f"\n  ✅ 验证通过！")
```

### Probability Calculation Pattern

```python
# ========== 步骤 N: 概率计算 ==========
prob = stats.norm.cdf(z_score)
print(f"📊 步骤 N: 概率计算")
print(f"  P(Z < {z_score:.2f}) = {prob:.4f}")
print(f"  即约 {prob*100:.1f}% 的数据低于该值")
```

### Chi-Square Test Pattern

```python
# ========== 步骤 N: 卡方检验 ==========
observed = np.array([...])
expected = np.array([...])

chi2_stat = np.sum((observed - expected)**2 / expected)
dof = len(observed) - 1
p_value = 1 - stats.chi2.cdf(chi2_stat, dof)

# Verify
chi2_scipy, p_scipy = stats.chisquare(observed, expected)
```

### ANOVA Pattern

```python
# ========== 步骤 N: 单因素方差分析 ==========
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f"📊 方差分析结果:")
print(f"  F 统计量 = {f_stat:.4f}")
print(f"  p 值 = {p_value:.6f}")

if p_value < alpha:
    print(f"\n  💡 至少有一组均值与其他组显著不同")
    # Post-hoc comparison
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    tukey = pairwise_tukeyhsd(data, groups, alpha=0.05)
    print(tukey)
```

### Non-Parametric Test Pattern

```python
# ========== 步骤 N: 非参数检验 ==========
# Always compare with parametric alternative
print("📊 参数检验 vs 非参数检验对比:")
print(f"\n  参数检验 (t 检验):")
t_stat, t_p = stats.ttest_ind(group1, group2)
print(f"    t = {t_stat:.4f}, p = {t_p:.4f}")

print(f"\n  非参数检验 (Wilcoxon 秩和):")
w_stat, w_p = stats.ranksums(group1, group2)
print(f"    W = {w_stat:.4f}, p = {w_p:.4f}")

print(f"\n  💡 当数据不满足正态性假设时，应使用非参数检验")
```

---

## 7. Quality Checklist

Before publishing a tutorial notebook, verify all items:

### Structure
- [ ] Title cell has 教学目标 (numbered list) + 参考书 + 教学策略
- [ ] Sections numbered sequentially with `## N.`
- [ ] Micro-example before scaled example
- [ ] 📌 核心概念回顾 section present (second-to-last)
- [ ] ❌ 常见误区 section present (last content section)
- [ ] At least 4-5 misconceptions listed

### Code
- [ ] All cells run top-to-bottom without errors
- [ ] `np.random.seed(42)` set in imports cell
- [ ] Every hand-calculation verified with scipy
- [ ] `# ========== Title ==========` headers on major code blocks
- [ ] `📊 步骤 N:` print format on computation steps

### Visualization
- [ ] All plot labels and titles in **English**
- [ ] Print explanations after `plt.show()` in **Chinese**
- [ ] `sns.set_style("whitegrid")` applied
- [ ] Figure titles have `fontweight='bold'`
- [ ] Green (#2ecc71) for positive/acceptance, Red (#e74c3c) for negative/rejection
- [ ] Grid alpha=0.3

### Markdown
- [ ] LaTeX formulas render correctly (test with `$$...$$`)
- [ ] Variables defined after every display-math formula
- [ ] Emoji usage consistent (📐📊💡📌🎯📖🔬)
- [ ] Comparison tables present where two methods are contrasted
- [ ] Book citations use `> blockquote` format

### Pedagogy
- [ ] Formula appears in MD cell **before** code implementation
- [ ] Micro→macro scaling present (10→25→200-500 items)
- [ ] DGP (data generating process) clearly documented in comments
- [ ] 回顾 section uses `📌` + definition/formula/interpretation format
- [ ] 误区 section uses `❌/✓` format
- [ ] scipy verification present for every hand-calculated statistic
