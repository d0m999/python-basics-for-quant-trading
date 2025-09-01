# pandas中迭代器的应用演示

import pandas as pd
import numpy as np

# 创建示例数据
print("=== pandas中的迭代器应用 ===")

# 创建Series
sales = pd.Series([100, 150, 200, 175, 300], 
                  index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                  name='Sales')

print("Sales Series:")
print(sales)
print(f"Series类型: {type(sales)}")

print(f"\n1. 迭代Series的值（默认行为）:")
for value in sales:
    print(f"销售额: {value}")

print(f"\n2. 迭代Series的索引:")
for index in sales.index:
    print(f"日期: {index}")

print(f"\n3. 迭代Series的索引-值对:")
for index, value in sales.items():
    print(f"{index}: {value}")

# 创建DataFrame
df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [10.5, 15.2, 8.9, 12.1],
    'Quantity': [100, 80, 150, 90]
})

print(f"\n=== DataFrame迭代 ===")
print("产品数据:")
print(df)

print(f"\n1. 迭代DataFrame的列名（默认行为）:")
for column in df:
    print(f"列名: {column}")

print(f"\n2. 迭代DataFrame的行（使用iterrows）:")
for index, row in df.iterrows():
    print(f"行 {index}: {row['Product']} - 价格: {row['Price']}, 数量: {row['Quantity']}")

print(f"\n3. 迭代DataFrame的行（使用itertuples，更高效）:")
for row in df.itertuples():
    print(f"行 {row.Index}: {row.Product} - 价格: {row.Price}, 数量: {row.Quantity}")

print(f"\n4. 迭代特定列的值:")
for product in df['Product']:
    print(f"产品: {product}")

# 演示迭代器在数据处理中的优势
print(f"\n=== 迭代器的内存优势演示 ===")

# 使用生成器表达式（基于迭代器）处理数据
large_data = range(1000000)  # 模拟大数据集
print(f"原始数据大小: {len(large_data)} 个元素")

# 内存友好的方式：使用生成器表达式
squared_generator = (x**2 for x in large_data if x % 1000 == 0)
print(f"生成器类型: {type(squared_generator)}")

print(f"前10个结果:")
count = 0
for result in squared_generator:
    if count >= 10:
        break
    print(f"平方值: {result}")
    count += 1

# 对比：列表推导式会占用大量内存
# squared_list = [x**2 for x in large_data if x % 1000 == 0]  # 这会占用很多内存

print(f"\n=== 自定义数据处理迭代器 ===")

class MovingAverage:
    """移动平均计算迭代器 - 常用的数据分析技术"""
    
    def __init__(self, data, window_size):
        self.data = data
        self.window_size = window_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + self.window_size > len(self.data):
            raise StopIteration
        
        # 计算当前窗口的平均值
        window_data = self.data[self.index:self.index + self.window_size]
        avg = sum(window_data) / len(window_data)
        
        self.index += 1
        return avg

# 使用移动平均迭代器
stock_prices = [100, 102, 98, 105, 107, 103, 99, 101, 104, 106]
print(f"股票价格: {stock_prices}")

ma_3 = MovingAverage(stock_prices, 3)
print(f"\n3日移动平均:")
for i, avg in enumerate(ma_3):
    print(f"第{i+1}个3日平均: {avg:.2f}")

# 使用pandas实现同样效果进行对比
print(f"\n使用pandas验证结果:")
prices_series = pd.Series(stock_prices)
pandas_ma3 = prices_series.rolling(window=3).mean().dropna()
print("pandas 3日移动平均:")
for i, avg in enumerate(pandas_ma3):
    print(f"第{i+1}个3日平均: {avg:.2f}")