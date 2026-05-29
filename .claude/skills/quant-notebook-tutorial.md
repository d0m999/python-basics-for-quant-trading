---
trigger: "notebook" OR "tutorial" OR "教程" OR "ipynb" OR "因子" OR "portfolio" OR "排序" OR "检验" OR "t-test" OR "量化绿皮书"
description: Concrete notebook construction workflow for quant/statistics tutorial notebooks. Covers cell structure, code patterns, visualization conventions, and quality checklist.
alwaysApply: false
---

# Quant Tutorial Notebook Construction Guide

This skill defines the **concrete notebook construction workflow** — cell organization, code idioms, markdown formatting, and visualization patterns. For pedagogical philosophy and teaching methodology, see `GEMINI.md`.

---

## 1. Notebook Skeleton

Every tutorial notebook follows this standard cell sequence:

```
Cell 0  [MD]   Title + 教学目标 + 参考书
Cell 1  [MD]   场景设定 / 动机 (🎯 问题)
Cell 2  [Code] Imports + 环境配置
Cell 3+ [MD]   Section headers with step-by-step content
        [Code] Micro-example (10-25 data points, hand-calc visible)
        [Code] Multi-period / scaled example (60-300 data points)
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

**参考书**：《[书名]》（[作者]）第 X 章
**教学策略**：先用极小数据集让你"看见"每一步计算，再扩展到真实规模
```

### Progressive Scaling Pattern

Notebooks must follow micro → macro scaling:

| Stage | Data Size | Purpose |
|-------|-----------|---------|
| Micro example | 10-25 items | Hand-calc every step, build intuition |
| Medium scale | 50-100 items | Show patterns emerging |
| Full simulation | 200-300 items × 60 months | T-test, statistical inference |

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
import seaborn as sns
from scipy import stats

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'DejaVu Sans']
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
# --- 每月生成新的截面数据 ---
# [Factor]: [distribution description]
factor_values = np.random.lognormal(mean=10, sigma=1, size=N_STOCKS)

# 收益率：包含因子效应 + 噪声
# 核心：[factor interpretation] → [return direction]
factor_effect = -0.3 * (log_factor - log_factor.mean())
noise = np.random.normal(0, 5, N_STOCKS)
returns = base_return + factor_effect + noise
```

Always document:
1. What distribution each variable follows
2. The sign and magnitude of factor effects
3. The noise level relative to signal

### groupby/apply Idioms

For conditional/dependent sorts:

```python
def conditional_sort(group):
    """在每个 [control variable] 组内部按 [target variable] 排序分组"""
    g = g.copy()
    g['target_group'] = pd.qcut(g['target'], N_GROUPS, labels=[...])
    return g

df = df.groupby('control_group', group_keys=False).apply(conditional_sort)
```

For cross-sectional portfolio returns:

```python
cross_rets = month_df.groupby(['group_a', 'group_b'])['return'].mean().unstack()
```

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
| Green | `#2ecc71` | Positive values, "good", acceptance |
| Red | `#e74c3c` | Negative values, rejection regions |
| Blue | `steelblue` | Neutral distributions, histograms |
| Orange | `#e67e22` | Warning, secondary emphasis |

For grouped bar charts, use sequential colormaps:

```python
colors = plt.cm.RdYlGn(np.linspace(0.15, 0.85, N_GROUPS))
# or
colors = plt.cm.RdYlGn_r(np.linspace(0.15, 0.85, N_GROUPS))
```

For Spread bar charts (positive/negative coloring):

```python
colors = ['#2ecc71' if s > 0 else '#e74c3c' for s in spreads]
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

### Heatmap Pattern

```python
sns.heatmap(matrix, annot=True, fmt='.2f', cmap='RdYlGn',
            linewidths=1, ax=ax, cbar_kws={'label': 'Return (%)'})
```

### Annotation Box Pattern

```python
textstr = f'Key Stat 1 = {val1:.3f}\nKey Stat 2 = {val2:.2f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
ax.text(0.98, 0.98, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', horizontalalignment='right', bbox=props)
```

### Bar Chart Value Labels

```python
for bar, v in zip(bars, values):
    va = 'bottom' if v >= 0 else 'top'
    offset = 0.1 if v >= 0 else -0.1
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + offset,
            f'{v:.2f}%', ha='center', va=va, fontweight='bold')
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

| Phase | Stocks | Months | Purpose |
|-------|--------|--------|---------|
| Micro | 10 | 1 | See every calculation |
| Small | 25 | 1 | See grouping mechanics |
| Full | 200-300 | 60 | Statistical inference |

Scale transitions use explicit print statements:

```python
print(f"📊 模拟参数：")
print(f"  股票数量: {N_STOCKS} 只/月")
print(f"  时间跨度: {N_MONTHS} 个月")
print(f"  分组数量: {N_GROUPS} 组")
```

### Section Flow for a Statistical Concept

```
1. 场景设定 (motivating question)
2. 公式推导 (LaTeX + variable definitions)
3. 微型数据手算 (10-25 items, print every step)
4. scipy 验证 (compare hand vs library)
5. 可视化 (English labels, Chinese print explanation)
6. 多期/大样本扩展 (60 months, full T-test)
7. 总结报告 (formatted summary)
```

---

## 6. Quant-Specific Patterns

### Factor Mimicking Portfolio (FMP) Construction

```python
# Standard FMP pattern
spread_t = group_returns['Q1'] - group_returns['Q5']  # Long-Short
monthly_spreads.append(spread_t)
```

Always explain FMP motivation:

```markdown
$$\text{FMP} = R_{\text{Long}} - R_{\text{Short}}$$

| 经典因子 | 做多 | 做空 | FMP 名称 |
|---------|------|------|----------|
| 市值因子 | 小市值股 | 大市值股 | SMB |
| 价值因子 | 高 B/M 股 | 低 B/M 股 | HML |
```

### T-Test on Spread Time Series

```python
# Standard pattern for factor significance test
spreads = np.array(monthly_spreads)
spread_mean = spreads.mean()
spread_std = spreads.std(ddof=1)
spread_se = spread_std / np.sqrt(N_MONTHS)
t_stat = spread_mean / spread_se
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=N_MONTHS-1))

# Verify
t_scipy, p_scipy = stats.ttest_1samp(spreads, 0)
```

### Monotonicity Test (Spearman)

```python
group_ranks = np.arange(1, N_GROUPS + 1)
group_ret_values = np.array([avg_rets[f'Q{i}'] for i in range(1, N_GROUPS+1)])
spearman_corr, spearman_p = stats.spearmanr(group_ranks, group_ret_values)
```

Interpretation thresholds:
- `|rho| > 0.8`: Strong monotonicity, factor quality excellent
- `|rho| > 0.5`: Moderate monotonicity
- `|rho| < 0.5`: Poor monotonicity, factor unreliable

### Economic Significance (Sharpe Ratio)

```python
sr_monthly = spread_mean / spread_std
sr_annual = sr_monthly * np.sqrt(12)
```

And the t-statistic relationship:

```python
# Verify: t = SR_monthly × sqrt(T)
print(f"  📐 验证: t = SR_monthly × √T = {sr_monthly:.4f} × √{N_MONTHS} = {sr_monthly * np.sqrt(N_MONTHS):.4f}")
```

### Confidence Interval Pattern

```python
t_critical = stats.t.ppf(0.975, df=df)
margin = t_critical * se
ci_lower = mean - margin
ci_upper = mean + margin
```

### Conditional (Dependent) Sort Idiom

```python
# Step 1: Control variable sort
df['control_group'] = pd.qcut(df['control_var'], N_GROUPS, labels=[...])

# Step 2: Within-group target variable sort
def cond_sort(g):
    g = g.copy()
    g['target_group'] = pd.qcut(g['target_var'], N_GROUPS, labels=[...])
    return g

df = df.groupby('control_group', group_keys=False).apply(cond_sort)

# Step 3: Cross returns and spread
cross_rets = df.groupby(['control_group', 'target_group'])['ret'].mean().unstack()
spread_per_control = cross_rets.iloc[:, -1] - cross_rets.iloc[:, 0]
avg_spread = spread_per_control.mean()
```

---

## 7. Quality Checklist

Before publishing a tutorial notebook, verify all items:

### Structure
- [ ] Title cell has 教学目标 (numbered list) + 参考书 + 教学策略
- [ ] Sections numbered sequentially with `## N.`
- [ ] Micro-example before multi-period example
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
- [ ] Green (#2ecc71) for positive, Red (#e74c3c) for negative
- [ ] Grid alpha=0.3

### Markdown
- [ ] LaTeX formulas render correctly (test with `$$...$$`)
- [ ] Variables defined after every display-math formula
- [ ] Emoji usage consistent (📐📊💡📌🎯📖)
- [ ] Comparison tables present where two methods are contrasted
- [ ] Book citations use `> blockquote` format

### Pedagogy
- [ ] Formula appears in MD cell **before** code implementation
- [ ] Micro→macro scaling present (10→25→200-300 items)
- [ ] DGP (data generating process) clearly documented in comments
- [ ] 回顾 section uses `📌` + definition/formula/interpretation format
- [ ] 误区 section uses `❌/✓` format
