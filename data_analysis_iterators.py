# 数据分析中的迭代器应用示例

import random

class DataBatch:
    """
    模拟数据分析中的批处理迭代器
    类似于机器学习中的数据批次处理
    """
    
    def __init__(self, data, batch_size=3):
        self.data = data
        self.batch_size = batch_size
    
    def __iter__(self):
        """返回批处理迭代器"""
        return BatchIterator(self.data, self.batch_size)
    
    def __len__(self):
        """返回总的批次数量"""
        return (len(self.data) + self.batch_size - 1) // self.batch_size

class BatchIterator:
    """批处理迭代器"""
    
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index >= len(self.data):
            raise StopIteration
        
        # 获取当前批次的数据
        end_index = min(self.current_index + self.batch_size, len(self.data))
        batch = self.data[self.current_index:end_index]
        self.current_index = end_index
        
        return batch

# 演示数据批处理
print("=== 数据批处理演示 ===")
sample_data = list(range(1, 21))  # 1到20的数据
print(f"原始数据: {sample_data}")
print(f"数据长度: {len(sample_data)}")

# 创建批处理迭代器
batch_processor = DataBatch(sample_data, batch_size=4)
print(f"批次数量: {len(batch_processor)}")

print("\n按批次处理数据:")
for batch_num, batch in enumerate(batch_processor, 1):
    batch_sum = sum(batch)
    batch_avg = batch_sum / len(batch)
    print(f"批次 {batch_num}: {batch} -> 总和={batch_sum}, 平均值={batch_avg:.2f}")

print("\n" + "="*60 + "\n")

# 模拟pandas Series的简化版本
class SimpleSeries:
    """简化版的pandas Series，展示迭代器在数据分析中的应用"""
    
    def __init__(self, data, index=None):
        self.data = list(data)
        self.index = index if index else list(range(len(data)))
        
        if len(self.data) != len(self.index):
            raise ValueError("数据和索引长度必须相等")
    
    def __iter__(self):
        """迭代数据值（模拟pandas Series的默认迭代行为）"""
        return iter(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data[key]
        elif key in self.index:
            idx = self.index.index(key)
            return self.data[idx]
        else:
            raise KeyError(f"键 '{key}' 不存在")
    
    def items(self):
        """返回(索引, 值)对的迭代器"""
        return zip(self.index, self.data)
    
    def keys(self):
        """返回索引的迭代器"""
        return iter(self.index)
    
    def values(self):
        """返回值的迭代器"""
        return iter(self.data)
    
    def __repr__(self):
        lines = []
        for idx, val in zip(self.index, self.data):
            lines.append(f"{idx}    {val}")
        return "\n".join(lines)

# 使用SimpleSeries
print("=== 简化版pandas Series演示 ===")
sales_data = SimpleSeries([100, 150, 200, 175, 300], 
                         index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'])

print("销售数据:")
print(sales_data)

print(f"\n数据长度: {len(sales_data)}")

print("\n迭代数据值（默认行为）:")
for value in sales_data:
    print(f"销售额: {value}")

print("\n迭代索引:")
for day in sales_data.keys():
    print(f"日期: {day}")

print("\n迭代索引-值对:")
for day, sales in sales_data.items():
    print(f"{day}: {sales}元")

print("\n通过索引访问:")
print(f"周一销售额: {sales_data['Mon']}")
print(f"第一天销售额: {sales_data[0]}")

print("\n" + "="*60 + "\n")

# 数据过滤迭代器示例
class FilteredIterator:
    """带过滤条件的迭代器，常用于数据清洗"""
    
    def __init__(self, data, filter_func):
        self.data = data
        self.filter_func = filter_func
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            current_item = self.data[self.index]
            self.index += 1
            
            if self.filter_func(current_item):
                return current_item
        
        raise StopIteration

class FilteredData:
    """支持过滤的数据集合"""
    
    def __init__(self, data):
        self.data = data
    
    def filter(self, condition):
        """返回满足条件的迭代器"""
        return FilteredIterator(self.data, condition)
    
    def __iter__(self):
        """默认返回所有数据"""
        return iter(self.data)

# 演示数据过滤
print("=== 数据过滤演示 ===")
exam_scores = FilteredData([85, 92, 78, 96, 88, 75, 90, 82, 94, 87])

print("所有成绩:")
for score in exam_scores:
    print(f"成绩: {score}")

print("\n优秀成绩（≥90分）:")
excellent_scores = exam_scores.filter(lambda x: x >= 90)
for score in excellent_scores:
    print(f"优秀成绩: {score}")

print("\n及格成绩（≥80分）:")
passing_scores = exam_scores.filter(lambda x: x >= 80)
passing_list = list(passing_scores)  # 转换为列表
print(f"及格成绩列表: {passing_list}")
print(f"及格人数: {len(passing_list)}")
print(f"及格率: {len(passing_list)/10*100:.1f}%")