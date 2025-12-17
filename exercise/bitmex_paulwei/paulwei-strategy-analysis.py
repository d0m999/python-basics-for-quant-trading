import pandas as pd
import numpy as np

# 读取数据
path_summary = '/Users/d0m999/Desktop/_bot/data_analysis/exercise/bitmex_paulwei/bitmex_account_summary.json'
path_executions = '/Users/d0m999/Desktop/_bot/data_analysis/exercise/bitmex_paulwei/bitmex_executions.csv'
path_trades = '/Users/d0m999/Desktop/_bot/data_analysis/exercise/bitmex_paulwei/bitmex_trades.csv'
path_orders = '/Users/d0m999/Desktop/_bot/data_analysis/exercise/bitmex_paulwei/bitmex_orders.csv'
path_wallet_history = '/Users/d0m999/Desktop/_bot/data_analysis/exercise/bitmex_paulwei/bitmex_wallet_history.csv'
# 使用json_normalize处理嵌套JSON数据
import json
with open(path_summary, 'r') as f:
    data = json.load(f)

account_summary = pd.json_normalize(data, max_level=1)
executions = pd.read_csv(path_executions)
trades = pd.read_csv(path_trades)
orders = pd.read_csv(path_orders)
wallet_history = pd.read_csv(path_wallet_history)

# 检查表格的缺失值
print(executions.isna().sum())
#print(trades.isna().sum())
#print(orders.isna().sum())
#print(wallet_history.isna().sum())

