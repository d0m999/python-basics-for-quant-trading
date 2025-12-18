import numpy as np
# 1. 设置数据
# 形状: (4, 2) 
arr1 = np.arange(8).reshape(4, 2)
print("=== 原始数据 (Shape: 4, 2) ===")
print(arr1)

# 形状变化: (4, 2) -> (2,) (第0轴消失)
mean0 = arr1.mean(axis=0)
print(f'--- Axis=0 ---\n形状: {mean0.shape}\n结果:\n{mean0}')

# 形状变化: (4, 2) -> (4,) (第1轴消失)
mean1 = arr1.mean(axis=1)
print(f'--- Axis=1 ---\n形状: {mean1.shape}\n结果:\n{mean1}')


# 1. 设置数据
# 形状: (2, 3, 4) 
# 隐喻: 2层蛋糕，每层有3行，每行4个切块
arr = np.arange(24).reshape(2, 3, 4)

print("=== 原始数据 (Shape: 2, 3, 4) ===")
print(arr)
print("\n" + "="*40 + "\n")

# 2. Axis = 0 (穿透/层聚合)
# 也就是将 Layer 0 和 Layer 1 对应位置相加
# 形状变化: (2, 3, 4) -> (3, 4) (第0轴消失)
res_0 = arr.sum(axis=0)
print(f"--- Axis=0 (穿透层) ---\n形状: {res_0.shape}\n结果:\n{res_0}")

# 3. Axis = 1 (垂直聚合/跨行)
# 在每一层内部，把"行"压扁
# 形状变化: (2, 3, 4) -> (2, 4) (第1轴消失)
res_1 = arr.sum(axis=1)
print(f"\n--- Axis=1 (层内跨行) ---\n形状: {res_1.shape}\n结果:\n{res_1}")

# 4. Axis = 2 (水平聚合/跨列)
# 在每一层内部，把"列"压扁
# 形状变化: (2, 3, 4) -> (2, 3) (第2轴消失)
res_2 = arr.sum(axis=2)
print(f"\n--- Axis=2 (层内跨列) ---\n形状: {res_2.shape}\n结果:\n{res_2}")
