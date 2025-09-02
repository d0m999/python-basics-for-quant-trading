# itertools.groupby 中函数参数详解

import itertools

def first_letter(x):
    return x[0]

names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

print("🎯 为什么 first_letter 不需要输入参数？")
print("=" * 50)

print("\n1. 函数对象 vs 函数调用的区别:")
print(f"   函数对象: {first_letter}")
print(f"   函数调用: {first_letter('Alan')}")
print(f"   是否可调用: {callable(first_letter)}")

print("\n2. itertools.groupby 的内部工作流程:")
print("   itertools.groupby(names, first_letter) 相当于:")
print("   for name in names:")
print("       key = first_letter(name)  # 这里才调用函数！")
print("       # 根据 key 进行分组")

print("\n3. 手动模拟 groupby 的过程:")
for i, name in enumerate(names, 1):
    key = first_letter(name)
    print(f"   步骤{i}: first_letter('{name}') -> '{key}'")

print("\n4. 实际的 groupby 结果:")
for letter, group_names in itertools.groupby(names, first_letter):
    print(f"   字母 '{letter}': {list(group_names)}")

print("\n5. 如果错误地传递函数调用结果:")
try:
    # 错误示例：传递函数调用结果
    result = first_letter("Alan")  # 返回 "A"
    # itertools.groupby(names, result)  # "A" 不是函数！
    print(f"   first_letter('Alan') 返回: '{result}' (类型: {type(result)})")
    print("   错误: 'A' 不是可调用对象，无法作为 key 函数使用")
except Exception as e:
    print(f"   错误: {e}")

print("\n🔍 核心理解:")
print("✅ 传递 first_letter     → 函数对象，可以被调用")  
print("❌ 传递 first_letter()  → 函数调用，返回具体值")

print("\n💡 这与你学过的方法引用概念一致:")
print("   str.strip        → 方法对象")
print("   str.strip(text)  → 方法调用")
print("   两者都是可调用对象，可以传递给其他函数使用！")