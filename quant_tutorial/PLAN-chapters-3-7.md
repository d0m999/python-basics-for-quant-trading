# 实现计划：《因子投资》第 3-7 章教程编写

## 📋 需求重述

按照 `quant_tutorial/` 目录下第 2 章（2.1-2.7）的教程风格，为《因子投资：方法与实践》（石川）第 3、4、5、6、7 章编写 Jupyter Notebook 教程。

## 📐 现有教程风格分析

从已有的 8 个教程（2.1-2.7 + t-test）中提取的核心模式：

| 维度 | 规范 |
|------|------|
| **文件命名** | `{chapter}.{section}-{topic}-tutorial.ipynb` |
| **标题格式** | `# [主题]完整教程：从 [简单] 到 [复杂]` |
| **教学目标** | 5 条编号列表，覆盖概念→手算→实现→验证→理解 |
| **参考书** | `《因子投资：方法与实践》（石川）第 X 章` |
| **数据缩放** | 微型（10-25）→ 中型（50-100）→ 完整模拟（200-300 × 60月） |
| **公式-代码顺序** | Markdown 公式 → 代码实现 → scipy 验证 |
| **结尾** | 📌 核心概念回顾 → ❌ 常见误区 |
| **可视化** | 英文标签 + 中文解释 |

---

## 📚 第 3-7 章内容与教程规划

### 第 3 章：风险模型 (Risk Models)

**核心主题**：协方差矩阵估计、Barra 风险模型、风险分解

| 教程编号 | 文件名 | 主题 | 复杂度 |
|---------|--------|------|--------|
| 3.1 | `3.1-covariance-estimation-tutorial.ipynb` | 协方差矩阵估计：从样本协方差到收缩估计 | 中 |
| 3.2 | `3.2-risk-decomposition-tutorial.ipynb` | 风险分解：系统性风险 vs 特质风险 | 中 |
| 3.3 | `3.3-barra-risk-model-tutorial.ipynb` | Barra 风险模型：多因子风险建模 | 高 |
| 3.4 | `3.4-factor-covariance-tutorial.ipynb` | 因子协方差矩阵的估计与正则化 | 高 |

**教学重点**：
- 3.1：样本协方差的不稳定性 → Ledoit-Wolf 收缩 → 手算收缩系数
- 3.2：组合风险的因子分解 → $R_p = \alpha + B'F + \epsilon$ → $\sigma_p^2 = B'\Sigma_F B + D$
- 3.3：Barra 因子体系 → 因子暴露矩阵 → 因子协方差 → 特质方差
- 3.4：指数加权移动平均 (EWMA) → Eigenfactor 风险调整 → 惩罚函数

---

### 第 4 章：因子投资组合构建 (Factor Portfolio Construction)

**核心主题**：组合优化、约束处理、换手率控制

| 教程编号 | 文件名 | 主题 | 复杂度 |
|---------|--------|------|--------|
| 4.1 | `4.1-factor-mimicking-portfolio-tutorial.ipynb` | 因子模拟投资组合：从排序法到优化法 | 中 |
| 4.2 | `4.2-portfolio-optimization-tutorial.ipynb` | 组合优化：均值-方差在因子投资中的应用 | 高 |
| 4.3 | `4.3-constraints-turnover-tutorial.ipynb` | 约束与换手率控制 | 高 |
| 4.4 | `4.4-tracking-error-tutorial.ipynb` | 跟踪误差与主动管理 | 中 |

**教学重点**：
- 4.1：FMP 的两种构建方式（排序 vs 优化）→ 权重计算 → 收益对比
- 4.2：目标函数 $\min w'B\Sigma_F B'w - \lambda w'Bf$ → KKT 条件 → scipy.optimize 验证
- 4.3：换手率惩罚 → 交易成本约束 → 持仓集中度限制
- 4.4：TE = $\sqrt{w'Vw}$ → TE 分解 → IR = $\alpha / TE$

---

### 第 5 章：业绩归因 (Performance Attribution)

**核心主题**：Brinson 归因、因子归因、风险归因

| 教程编号 | 文件名 | 主题 | 复杂度 |
|---------|--------|------|--------|
| 5.1 | `5.1-brinson-attribution-tutorial.ipynb` | Brinson 归因：选股收益 vs 择时收益 | 中 |
| 5.2 | `5.2-factor-attribution-tutorial.ipynb` | 因子归因：收益的因子来源分解 | 中 |
| 5.3 | `5.3-risk-attribution-tutorial.ipynb` | 风险归因：风险的因子来源分解 | 高 |

**教学重点**：
- 5.1：BHB 模型 → 选股效应 + 交互效应 + 择时效应 → 手算 3 只股票 2 行业
- 5.2：$R_p = \alpha + \sum_k \beta_k f_k + \epsilon$ → 因子贡献 = $\beta_k f_k / R_p$
- 5.3：边际风险贡献 (MCTR) → $\text{MCTR}_k = \frac{(B\Sigma_F)_k}{\sigma_p}$ → 风险分解

---

### 第 6 章：机器学习与因子投资 (ML in Factor Investing)

**核心主题**：特征工程、模型选择、过拟合防范

| 教程编号 | 文件名 | 主题 | 复杂度 |
|---------|--------|------|--------|
| 6.1 | `6.1-feature-engineering-tutorial.ipynb` | 因子特征工程：从原始数据到因子特征 | 中 |
| 6.2 | `6.2-ml-factor-selection-tutorial.ipynb` | 机器学习因子选择：LASSO, Ridge, ElasticNet | 高 |
| 6.3 | `6.3-tree-models-tutorial.ipynb` | 树模型在因子投资中的应用：RF, XGBoost | 高 |
| 6.4 | `6.4-cross-validation-finance-tutorial.ipynb` | 金融领域的交叉验证：时序分割与防前视偏差 | 中 |

**教学重点**：
- 6.1：原始特征 → 行业中性化 → 标准化 → 缺失值处理 → 特征组合
- 6.2：正则化原理 → LASSO 路径图 → 时序滚动训练 → IC 评估
- 6.3：特征重要性 → SHAP 值 → 与线性模型对比
- 6.4：Purged K-Fold → Embargo → Combinatorial Purged CV

---

### 第 7 章：因子投资实践 (Factor Investment Practice)

**核心主题**：A 股实证、因子构建全流程、策略回测

| 教程编号 | 文件名 | 主题 | 复杂度 |
|---------|--------|------|--------|
| 7.1 | `7.1-a-share-factors-tutorial.ipynb` | A 股常见因子构建：市值、价值、动量 | 中 |
| 7.2 | `7.2-full-pipeline-tutorial.ipynb` | 因子研究全流程：从数据到结论 | 高 |
| 7.3 | `7.3-backtest-engine-tutorial.ipynb` | 回测引擎：从信号到净值 | 高 |

**教学重点**：
- 7.1：A 股数据获取 → 行业分类 → 因子计算 → IC/排序检验
- 7.2：数据清洗 → 因子计算 → 单因子检验 → 多因子模型 → 组合构建
- 7.3：信号生成 → 权重计算 → 收益计算 → 绩效指标 → 可视化

---

## ⚠️ 风险评估

| 风险 | 级别 | 缓解措施 |
|------|------|---------|
| PDF 无法直接读取，章节内容可能有偏差 | **高** | 需确认每章具体小节后再细化 |
| 第 6 章 ML 内容需要额外依赖（sklearn, xgboost） | **中** | 统一依赖管理，Cell 2 import 模板 |
| 第 7 章需要真实 A 股数据 | **中** | 可用 tushare/akshare 或合成数据模拟 |
| 部分章节（如 Barra）涉及专利模型 | **低** | 教授公开可得的简化版本 |
| 教程数量多（约 18 个 notebook），工作量大 | **高** | 按章节分批编写，优先核心章节 |

---

## 📅 建议执行顺序

```
Phase 1 (第 5 章 业绩归因) → 与第 2 章知识直接衔接，难度适中
Phase 2 (第 3 章 风险模型) → 组合构建的前置知识
Phase 3 (第 4 章 组合构建) → 依赖第 3 章风险模型
Phase 4 (第 7 章 实践)    → 综合运用前 4 章知识
Phase 5 (第 6 章 机器学习) → 独立性最强，可最后编写
```

---

## 📏 每个 Notebook 的标准结构

```
Cell 0  [MD]   # 标题 + 教学目标(5条) + 参考书 + 教学策略
Cell 1  [MD]   ## 1. 场景设定 / 动机 (🎯 问题)
Cell 2  [Code] Imports + 环境配置 (np.random.seed(42))
Cell 3+ [MD/Code]  ## 2-8 步骤内容
                → 📐 公式 (MD)
                → 📊 微型手算 (Code, 10-25 数据点)
                → 🔬 scipy/库验证 (Code)
                → 📊 扩展到真实规模 (Code, 200-300 × 60月)
                → 📈 可视化 (Code, 英文标签)
                → 💡 解释 (MD)
Cell N-2 [MD]  📌 核心概念回顾
Cell N-1 [MD]  ❌ 常见误区 (4-5条)
```

---

## ⏱️ 复杂度估算

| 章节 | 教程数 | 预估总 Cell 数 | 预估工作量 |
|------|--------|---------------|-----------|
| 第 3 章 | 4 | ~120 | 高 |
| 第 4 章 | 4 | ~130 | 高 |
| 第 5 章 | 3 | ~90 | 中 |
| 第 6 章 | 4 | ~140 | 高 |
| 第 7 章 | 3 | ~100 | 中高 |
| **总计** | **18** | **~580** | **约 60-80 小时** |
