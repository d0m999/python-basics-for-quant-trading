# itertools.groupby 中函数参数的详细解释

import itertools

def first_letter(x):
    return x[0]

names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

print("=" * 60)
print("1. 理解函数对象 vs 函数调用")
print("=" * 60)

# 函数对象（可调用对象）
print(f"first_letter 是什么: {first_letter}")
print(f"first_letter 的类型: {type(first_letter)}")
print(f"first_letter 是否可调用: {callable(first_letter)}")

# 函数调用的结果
print(f"first_letter('Alan') 是什么: {first_letter('Alan')}")
print(f"first_letter('Alan') 的类型: {type(first_letter('Alan'))}")

print("\n" + "=" * 60)
print("2. itertools.groupby 的工作原理")
print("=" * 60)

print("itertools.groupby(iterable, key_func) 的工作过程:")
print("1. 遍历 iterable 中的每个元素")
print("2. 对每个元素调用 key_func(element)")
print("3. 根据 key_func 的返回值进行分组")

print("\n手动模拟 groupby 的工作过程:")
for i, name in enumerate(names):
    print(f"步骤 {i+1}: first_letter('{name}') = '{first_letter(name)}'")

print("\n" + "=" * 60)
print("3. 实际的 groupby 结果")
print("=" * 60)

# 实际使用 groupby
for letter, group_names in itertools.groupby(names, first_letter):
    print(f"字母 '{letter}': {list(group_names)}")

print("\n" + "=" * 60)
print("4. 错误示例：如果传递函数调用结果会怎样")
print("=" * 60)

try:
    # 错误：传递函数调用的结果而不是函数对象
    # first_letter("Alan") 返回 "A"，这不是一个函数
    for letter, group_names in itertools.groupby(names, first_letter("Alan")):
        print(f"字母 '{letter}': {list(group_names)}")
except TypeError as e:
    print(f"错误: {e}")
    print("原因: 'A' 不是一个可调用的函数")

print("\n" + "=" * 60)
print("5. 不同的 key 函数示例")
print("=" * 60)

# 使用内置函数 len
print("按名字长度分组:")
for length, group_names in itertools.groupby(sorted(names, key=len), len):
    print(f"长度 {length}: {list(group_names)}")

# 使用 lambda 函数
print("\n按名字最后一个字母分组:")
names_sorted_by_last = sorted(names, key=lambda x: x[-1])
for last_letter, group_names in itertools.groupby(names_sorted_by_last, lambda x: x[-1]):
    print(f"最后字母 '{last_letter}': {list(group_names)}")

# 使用字符串方法
print("\n按名字长度分组（使用字符串方法）:")
names_by_length = sorted(names, key=str.__len__)  # 方法引用！
for length, group_names in itertools.groupby(names_by_length, str.__len__):
    print(f"长度 {length}: {list(group_names)}")

print("\n" + "=" * 60)
print("6. 方法引用的概念（对应你的学习要点）")
print("=" * 60)

print("就像你学过的 str.strip 一样，函数名本身就是一个对象:")
print(f"str.strip: {str.strip}")
print(f"str.__len__: {str.__len__}")
print(f"first_letter: {first_letter}")

print("\n这些都是可调用的对象，可以传递给其他函数:")
text = "  hello  "
print(f"text.strip(): '{text.strip()}'")
print(f"str.strip(text): '{str.strip(text)}'")  # 等价调用

# 同样，first_letter 也是可调用对象
name = "Alan"
print(f"first_letter(name): '{first_letter(name)}'")

print("\n" + "=" * 60)
print("7. 自定义 groupby 实现（理解原理）")
print("=" * 60)

def my_groupby(iterable, key_func):
    """简化版的 groupby 实现"""
    result = {}
    for item in iterable:
        # 关键：这里调用 key_func(item)
        key = key_func(item)  # 等价于 first_letter(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result.items()

print("使用自定义 groupby:")
for letter, group_names in my_groupby(names, first_letter):
    print(f"字母 '{letter}': {group_names}")

print("\n" + "=" * 60)
print("8. 总结")
print("=" * 60)

print("""
🎯 核心要点:
1. first_letter 是函数对象，不是函数调用
2. itertools.groupby 内部会调用 first_letter(每个元素)
3. 这就是为什么传递 first_letter 而不是 first_letter()
4. 函数对象可以像变量一样传递和引用

📝 类比理解:
- first_letter 就像一个"工具"
- itertools.groupby 拿到这个"工具"后，对每个元素使用这个工具
- 你只需要告诉它用什么工具，不需要你亲自使用工具

这与 str.strip 等方法引用的概念完全一致！
""")