# Pandas 完整语法结构参考指南

## 📚 核心数据操作方法

### 1. **.drop()** - 删除行或列
```python
DataFrame.drop(labels=None, axis=0, index=None, columns=None, 
               level=None, inplace=False, errors='raise')
```

**参数说明**:
- `labels`: 要删除的标签（单值或列表）
- `axis`: 0=删除行, 1=删除列 (默认0)
- `index`: 删除特定行标签 (axis=0时)
- `columns`: 删除特定列标签 (axis=1时)
- `inplace`: 是否原地修改，True=直接修改原对象节省内存但数据不可恢复，False=创建新副本保护数据但占用更多内存 (默认False)
- `errors`: 'ignore'或'raise' (默认'raise')

**示例**:
```python
# 删除行
df.drop([0, 1, 2])                    # 删除索引0,1,2的行
df.drop(index=['A', 'B'])             # 删除标签为'A','B'的行

# 删除列
df.drop(['col1', 'col2'], axis=1)     # 删除'col1','col2'列
df.drop(columns=['age', 'name'])      # 删除'age','name'列

# 原地删除
df.drop(['col1'], axis=1, inplace=True)
```

---

### 2. **.set_index()** - 设置索引
```python
DataFrame.set_index(keys, drop=True, append=False, 
                    inplace=False, verify_integrity=False)
```

**参数说明**:
- `keys`: 列名或列的列表，作为新索引
- `drop`: 是否删除原列 (默认True)
- `append`: 是否保留原索引 (默认False)
- `inplace`: 是否原地修改，True=直接修改原对象节省内存但数据不可恢复，False=创建新副本保护数据但占用更多内存 (默认False)
- `verify_integrity`: 是否检查重复值 (默认False)

**示例**:
```python
# 设置单列索引
df.set_index('ID')                    # 以'ID'列作为索引

# 设置多级索引
df.set_index(['Year', 'Month'])       # 创建多级索引

# 保留原索引并追加
df.set_index('ID', append=True)       # 保留原索引，追加新索引

# 不删除原列
df.set_index('ID', drop=False)        # 保留'ID'列
```

---

### 3. **.reset_index()** - 重置索引
```python
DataFrame.reset_index(level=None, drop=False, 
                     inplace=False, col_level=0, col_fill='')
```

**参数说明**:
- `level`: 重置的级别 (默认None，重置所有级别)
- `drop`: 是否丢弃索引 (默认False，保留为列)
- `inplace`: 是否原地修改，True=直接修改原对象节省内存但数据不可恢复，False=创建新副本保护数据但占用更多内存 (默认False)
- `col_level`: 多级列名的级别
- `col_fill`: 多级列名的填充字符

**示例**:
```python
# 重置为普通列
df.reset_index()                      # 将索引转换为列

# 丢弃索引
df.reset_index(drop=True)             # 完全删除索引

# 重置多级索引的特定级别
df.reset_index(level=0)               # 只重置第一级索引
```

---

### 4. **.loc[]** - 标签索引
```python
DataFrame.loc[row_selector, column_selector]
```

**用法示例**:
```python
# 单个标签
df.loc['A']                           # 获取行'A'
df.loc['A', 'col1']                   # 获取单元格('A','col1')

# 标签列表
df.loc[['A', 'B']]                    # 获取行'A','B'
df.loc[['A', 'B'], ['col1', 'col2']]  # 获取子DataFrame

# 标签范围 (包含端点)
df.loc['A':'C']                       # 从'A'到'C'的所有行
df.loc['A':'C', 'col1':'col3']        # 行范围和列范围

# 条件选择
df.loc[df['col1'] > 10]               # 条件行选择
df.loc[df['col1'] > 10, 'col2']       # 条件选择特定列
```

---

### 5. **.iloc[]** - 位置索引
```python
DataFrame.iloc[row_selector, column_selector]
```

**用法示例**:
```python
# 单个位置
df.iloc[0]                            # 获取第0行
df.iloc[0, 1]                         # 获取第0行第1列

# 位置列表
df.iloc[[0, 1, 2]]                    # 获取第0,1,2行
df.iloc[[0, 1], [0, 1]]               # 获取子DataFrame

# 位置范围 (不包含结束位置)
df.iloc[0:3]                          # 获取第0,1,2行
df.iloc[0:3, 1:4]                     # 行范围和列范围

# 布尔数组选择
df.iloc[[True, False, True]]          # 布尔数组行选择
```

---

### 6. **.query()** - 查询数据
```python
DataFrame.query(expr, inplace=False, **kwargs)
```

**参数说明**:
- `expr`: 查询表达式字符串
- `inplace`: 是否原地修改，True=直接修改原对象节省内存但数据不可恢复，False=创建新副本保护数据但占用更多内存 (默认False)

**示例**:
```python
# 基本查询
df.query('col1 > 10')                 # col1 > 10的行

# 多条件查询
df.query('col1 > 10 and col2 < 5')    # 复合条件
df.query('col1 > 10 or col2 < 5')     # 或条件

# 字符串查询
df.query('name == "Alice"')           # 字符串匹配
df.query('name in ["Alice", "Bob"]')  # 列表包含

# 外部变量引用
value = 10
df.query('col1 > @value')             # 使用外部变量
```

---

### 7. **.sort_values()** - 排序
```python
DataFrame.sort_values(by, axis=0, ascending=True, 
                     inplace=False, kind='quicksort', 
                     na_position='last', ignore_index=False)
```

**参数说明**:
- `by`: 排序的列名或列名列表
- `axis`: 0=按行排序, 1=按列排序 (默认0)
- `ascending`: 升序 (默认True)
- `kind`: 排序算法 (默认'quicksort')
- `na_position`: NaN位置 (默认'last')
- `ignore_index`: 是否重置索引 (默认False)

**示例**:
```python
# 单列排序
df.sort_values('col1')                # 按col1升序排序
df.sort_values('col1', ascending=False) # 按col1降序排序

# 多列排序
df.sort_values(['col1', 'col2'])      # 先按col1，再按col2
df.sort_values(['col1', 'col2'], ascending=[True, False]) # 不同排序方向

# 忽略NaN
df.sort_values('col1', na_position='first') # NaN放前面
```

---

### 8. **.groupby()** - 分组操作
```python
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, 
                 sort=True, group_keys=True, squeeze=False, 
                 observed=False, dropna=True)
```

**参数说明**:
- `by`: 分组键 (列名、列表或函数)
- `as_index`: 是否将分组键作为索引 (默认True)
- `sort`: 是否对分组键排序 (默认True)
- `dropna`: 是否删除NaN分组 (默认True)

**示例**:
```python
# 基本分组
df.groupby('category').sum()          # 按category分组求和
df.groupby('category')['value'].mean() # 按category分组求value均值

# 多列分组
df.groupby(['category', 'region']).agg({
    'value': ['sum', 'mean'],
    'count': 'size'
})

# 自定义分组函数
df.groupby(lambda x: x % 2).sum()     # 按奇偶索引分组
```

---

### 9. **.merge()** - 合并DataFrame
```python
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None,
               left_index=False, right_index=False, sort=False,
               suffixes=('_x', '_y'), copy=True, indicator=False,
               validate=None)
```

**参数说明**:
- `right`: 要合并的DataFrame
- `how`: 连接方式 ('left','right','outer','inner','cross')
- `on`: 连接键 (列名或列名列表)
- `left_on/right_on`: 左右DataFrame的连接键
- `suffixes`: 重名列的后缀

**示例**:
```python
# 等值连接
df1.merge(df2, on='key')              # 内连接
df1.merge(df2, how='left', on='key')  # 左连接

# 不同列名连接
df1.merge(df2, left_on='key1', right_on='key2')

# 多键连接
df1.merge(df2, on=['key1', 'key2'])
```

---

### 10. **.concat()** - 连接DataFrame
```python
pandas.concat(objs, axis=0, ignore_index=False, keys=None,
             levels=None, names=None, verify_integrity=False,
             sort=False, copy=True)
```

**参数说明**:
- `objs`: 要连接的DataFrame列表
- `axis`: 0=垂直连接, 1=水平连接
- `ignore_index`: 是否忽略原索引 (默认False)
- `keys`: 创建多级索引的键

**示例**:
```python
# 垂直连接
pd.concat([df1, df2, df3])            # 沿轴0连接
pd.concat([df1, df2], ignore_index=True) # 重置索引

# 水平连接
pd.concat([df1, df4], axis=1)         # 沿轴1连接

# 创建多级索引
pd.concat([df1, df2], keys=['first', 'second'])
```

---

## 📊 数据变形方法

### 11. **.pivot()** - 透视表
```python
DataFrame.pivot(index=None, columns=None, values=None)
```

**参数说明**:
- `index`: 新索引的列
- `columns`: 新列的列
- `values`: 填充值的列

**示例**:
```python
# 基本透视
df.pivot(index='date', columns='variable', values='value')

# 多值透视
df.pivot(index='date', columns='variable', 
         values=['value1', 'value2'])
```

---

### 12. **.melt()** - 融化(反透视)
```python
DataFrame.melt(id_vars=None, value_vars=None, 
               var_name=None, value_name='value')
```

**参数说明**:
- `id_vars`: 保持不变的列
- `value_vars`: 要融化的列
- `var_name`: 变量列名 (默认'variable')
- `value_name`: 值列名 (默认'value')

**示例**:
```python
# 基本融化
df.melt(id_vars=['ID'], var_name='variable', value_name='value')

# 只融化指定列
df.melt(value_vars=['col1', 'col2'])
```

---

## 🔧 数据清洗方法

### 13. **.fillna()** - 填充缺失值
```python
DataFrame.fillna(value=None, method=None, axis=None,
                inplace=False, limit=None, downcast=None)
```

**参数说明**:
- `value`: 填充值
- `method`: 填充方法 ('ffill','bfill','pad','backfill')
- `limit`: 填充的最大连续数量

**示例**:
```python
# 固定值填充
df.fillna(0)                          # 用0填充所有NaN
df.fillna({'col1': 0, 'col2': 'N/A'}) # 不同列用不同值

# 前向/后向填充
df.fillna(method='ffill')             # 用前一个值填充
df.fillna(method='bfill')             # 用后一个值填充

# 统计值填充
df.fillna(df.mean())                  # 用均值填充
df.fillna(df.median())                # 用中位数填充
```

---

### 14. **.dropna()** - 删除缺失值
```python
DataFrame.dropna(axis=0, how='any', thresh=None, 
                subset=None, inplace=False)
```

**参数说明**:
- `axis`: 0=删除包含NaN的行, 1=删除包含NaN的列
- `how`: 'any'=任意NaN, 'all'=全为NaN
- `thresh`: 非NaN值的最小数量
- `subset`: 检查的列子集

**示例**:
```python
# 删除包含NaN的行
df.dropna()                           # 删除任意包含NaN的行
df.dropna(how='all')                  # 删除全为NaN的行
df.dropna(thresh=3)                   # 保留至少有3个非NaN值的行

# 删除包含NaN的列
df.dropna(axis=1)                     # 删除任意包含NaN的列

# 特定列检查
df.dropna(subset=['col1', 'col2'])    # 只检查col1,col2列
```

---

### 15. **.astype()** - 类型转换
```python
DataFrame.astype(dtype, copy=True, errors='raise')
```

**参数说明**:
- `dtype`: 目标数据类型或字典
- `copy`: 是否创建副本 (默认True)
- `errors`: 'ignore'或'raise' (默认'raise')

**示例**:
```python
# 单列转换
df['col1'].astype('int64')            # 转换为int64

# 整列转换
df.astype({'col1': 'int64', 'col2': 'float64'})

# 转换时忽略错误
df.astype('int64', errors='ignore')
```

---

## 🧮 数据计算方法

### 16. **.apply()** - 应用函数
```python
DataFrame.apply(func, axis=0, raw=False, result_type=None, 
               args=(), **kwargs)
```

**参数说明**:
- `func`: 要应用的函数
- `axis`: 0=按列应用, 1=按行应用
- `raw`: 是否传递原始数组 (默认False)
- `result_type`: 'expand','reduce','broadcast'

**示例**:
```python
# 按列应用函数
df.apply(lambda x: x.max() - x.min()) # 每列的极差

# 按行应用函数
df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# 使用内置函数
df.apply('sum')                       # 每列求和
df.apply('mean', axis=1)              # 每行求均值
```

---

### 17. **.map()** - 元素映射
```python
Series.map(arg, na_action=None)
```

**参数说明**:
- `arg`: 映射关系 (字典、函数或Series)
- `na_action`: 处理NaN的方法 ('ignore'或None)

**示例**:
```python
# 字典映射
df['col1'].map({'A': 1, 'B': 2, 'C': 3})

# 函数映射
df['col1'].map(lambda x: x * 2)

# Series映射
mapping_series = pd.Series({'A': 1, 'B': 2})
df['col1'].map(mapping_series)
```

---

### 18. **.rename()** - 重命名
```python
DataFrame.rename(mapper=None, index=None, columns=None, 
                axis=None, copy=True, inplace=False, 
                level=None, errors='ignore')
```

**参数说明**:
- `mapper`: 重命名函数或字典
- `index`: 索引重命名
- `columns`: 列名重命名
- `axis`: 指定轴 (0=行, 1=列)

**示例**:
```python
# 字典重命名列
df.rename(columns={'old_name': 'new_name', 'col2': 'col_2'})

# 函数重命名
df.rename(str.upper, axis=1)          # 列名转大写
df.rename(lambda x: f'new_{x}')       # 索引重命名

# 指定轴重命名
df.rename(index={0: 'A', 1: 'B'})     # 重命名行索引
```

---

### 19. **.assign()** - 创建新列
```python
DataFrame.assign(**kwargs)
```

**参数说明**:
- `**kwargs`: 新列名=值的键值对

**示例**:
```python
# 创建新列
df.assign(total = df['col1'] + df['col2'])
df.assign(
    ratio = lambda x: x['col1'] / x['col2'],
    log_col1 = lambda x: np.log(x['col1'])
)

# 多个新列
df.assign(
    col3 = df['col1'] * 2,
    col4 = df['col2'] - 10
)
```

---

### 20. **.select_dtypes()** - 选择数据类型
```python
DataFrame.select_dtypes(include=None, exclude=None)
```

**参数说明**:
- `include`: 包含的数据类型
- `exclude`: 排除的数据类型

**示例**:
```python
# 选择数值列
df.select_dtypes(include=[np.number])

# 排除字符串列
df.select_dtypes(exclude=['object'])

# 组合选择
df.select_dtypes(include=['int64', 'float64'], exclude=['int32'])

# 使用字符串
df.select_dtypes(include='number')
df.select_dtypes(exclude='datetime')
```

---

## 🎯 实用技巧总结

### **方法链式调用示例**
```python
# 数据处理管道
result = (df
    .query('value > 0')               # 过滤数据
    .assign(log_value = lambda x: np.log(x['value']))
    .groupby('category')['log_value']
    .agg(['mean', 'std', 'count'])
    .reset_index()
    .rename(columns={'mean': 'avg_log', 'std': 'std_log'})
    .sort_values('avg_log', ascending=False)
)
```

### **常见错误处理**
```python
# 安全的数据访问
df.loc[df.index.isin(['A', 'B']), 'col1']  # 检查索引是否存在

# 处理重复索引
df = df[~df.index.duplicated(keep='first')]

# 内存优化
df = df.astype({'col1': 'category'})      # 减少内存使用
```

这份指南涵盖了pandas中最常用方法的完整语法结构。每个方法都提供了详细的参数说明和实用示例，帮助您更好地理解和使用pandas进行数据分析。