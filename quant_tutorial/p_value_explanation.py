"""
P 值计算与可视化 — 独立精简版
================================
本脚本是 t-test-tutorial.ipynb 中 P 值相关部分的精简独立版本。
可以脱离 notebook 单独运行，适合快速查阅 P 值的计算方式和图形化理解。
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 设置参数
t_statistic = -2.5  # 假设 T 值
degrees_of_freedom = 10
alpha = 0.05

# 计算不同方式的 P 值
print("=" * 60)
print("P 值的不同计算方式")
print("=" * 60)

# 方法 1: 使用 scipy 的 ttest_1samp (双尾)
print(f"\n假设 T 统计量 = {t_statistic}, 自由度 = {degrees_of_freedom}")
print(f"\n方法 1: 使用 scipy.stats.t.cdf")
abs_t = abs(t_statistic)
left_tail = stats.t.cdf(-abs_t, df=degrees_of_freedom)
right_tail = 1 - stats.t.cdf(abs_t, df=degrees_of_freedom)
p_value_manual = left_tail + right_tail

print(f"  左侧尾部面积 (T ≤ {-abs_t}): {left_tail:.6f}")
print(f"  右侧尾部面积 (T ≥ {abs_t}):  {right_tail:.6f}")
print(f"  P 值 (左侧 + 右侧): {p_value_manual:.6f}")

# 方法 2: 使用 scipy 的 sf (survival function)
p_value_sf = 2 * stats.t.sf(abs_t, df=degrees_of_freedom)
print(f"\n方法 2: 使用 scipy.stats.t.sf (生存函数)")
print(f"  sf(|t|) = P(T ≥ |t|): {stats.t.sf(abs_t, df=degrees_of_freedom):.6f}")
print(f"  P 值 = 2 × sf(|t|): {p_value_sf:.6f}")

# 方法 3: 直接计算
p_value_direct = 2 * (1 - stats.t.cdf(abs_t, df=degrees_of_freedom))
print(f"\n方法 3: 直接计算")
print(f"  P 值 = 2 × (1 - CDF(|t|)): {p_value_direct:.6f}")

print(f"\n✅ 三种方法结果一致: {p_value_manual == p_value_sf == p_value_direct}")

# ========================================
# 可视化 P 值
# ========================================
fig, ax = plt.subplots(figsize=(12, 6))

x = np.linspace(-4, 4, 1000)
t_dist = stats.t.pdf(x, df=degrees_of_freedom)

# 绘制 T 分布
ax.plot(x, t_dist, 'b-', linewidth=2, label=f'T distribution (df={degrees_of_freedom})')

# 标记 T 值位置
abs_t = abs(t_statistic)
ax.axvline(x=t_statistic, color='red', linestyle='--', linewidth=2, 
            label=f'T value = {t_statistic}')
ax.axvline(x=-t_statistic, color='red', linestyle='--', linewidth=2)
ax.axvline(x=0, color='black', linestyle='-', linewidth=0.5, alpha=0.5)

# 填充尾部区域 (P 值)
ax.fill_between(x, t_dist, where=(x <= -abs_t), 
                color='red', alpha=0.4, 
                label=f'Left tail\nArea = {left_tail:.4f}')
ax.fill_between(x, t_dist, where=(x >= abs_t), 
                color='red', alpha=0.4, 
                label=f'Right tail\nArea = {right_tail:.4f}')

# 标注总面积
ax.text(0, max(t_dist)*0.9, f'Total area = 1.0', 
        ha='center', va='center', fontsize=10, 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 标注 P 值
ax.text(0.5, min(t_dist)/2, f'P value = {p_value_manual:.4f}\n= Left tail + Right tail\n= {left_tail:.4f} + {right_tail:.4f}', 
        ha='center', va='center', fontsize=11, 
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

ax.set_xlabel('T Value', fontsize=12)
ax.set_ylabel('Probability Density', fontsize=12)
ax.set_title(f'Understanding P Value (T = {t_statistic}, df = {degrees_of_freedom})', 
             fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ========================================
# 与临界值对比
# ========================================
print("\n" + "=" * 60)
print("P 值与临界值的关系")
print("=" * 60)

critical_value = stats.t.ppf(1 - alpha/2, df=degrees_of_freedom)
print(f"\n显著性水平 α = {alpha}")
print(f"临界值 = ±{critical_value:.4f}")
print(f"\n我们的 T 值 = {t_statistic:.4f}")
print(f"|T| = {abs_t:.4f}")

if abs_t > critical_value:
    print(f"\n✓ |T| > 临界值 ({abs_t:.4f} > {critical_value:.4f})")
    print(f"✓ P 值 ({p_value_manual:.6f}) < α ({alpha})")
    print(f"✓ 拒绝原假设")
else:
    print(f"\n✗ |T| ≤ 临界值 ({abs_t:.4f} ≤ {critical_value:.4f})")
    print(f"✗ P 值 ({p_value_manual:.6f}) ≥ α ({alpha})")
    print(f"✗ 不能拒绝原假设")

# ========================================
# 面积关系说明
# ========================================
print("\n" + "=" * 60)
print("面积关系说明")
print("=" * 60)
print(f"\nT 分布总面积: 1.0 (100%)")
print(f"左侧尾部面积: {left_tail:.6f} ({left_tail*100:.2f}%)")
print(f"右侧尾部面积: {right_tail:.6f} ({right_tail*100:.2f}%)")
print(f"P 值 (两个尾部之和): {p_value_manual:.6f} ({p_value_manual*100:.2f}%)")
print(f"中间区域面积: {1 - p_value_manual:.6f} ({(1-p_value_manual)*100:.2f}%)")

print(f"\n💡 关键理解:")
print(f"   1. P 值 = 左侧尾部 + 右侧尾部")
print(f"   2. 不是'占总面积的比例'，而是两个尾部面积的绝对值")
print(f"   3. 总面积 = 1，所以 P 值本身就是一个概率值")
print(f"   4. P < 0.05 意味着两个尾部面积之和小于 5%")

# ========================================
# 不同 T 值的 P 值对比
# ========================================
print("\n" + "=" * 60)
print("不同 T 值对应的 P 值")
print("=" * 60)

t_values = [0, 1, 1.96, 2.262, 2.5, 3, 4]
print(f"\n{'T 值':<10} {'P 值':<15} {'显著性':<10}")
print("-" * 40)

for t in t_values:
    p = 2 * (1 - stats.t.cdf(abs(t), df=degrees_of_freedom))
    sig = "✓" if p < 0.05 else "✗"
    print(f"{t:<10.2f} {p:<15.6f} {sig:<10}")

print(f"\n临界值 = {critical_value:.4f} (对应 P = {alpha})")