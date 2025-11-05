import json
import os
import pandas as pd
from collections import OrderedDict

with open('final_results.json', 'r') as f:
    data = json.load(f)

avg_acc = data['avg_acc']
avg_acc_mean = data['avg_acc_mean']

last_acc = data['last_acc:']
last_acc_mean = data['last_acc_mean']

print(last_acc)
print(last_acc_mean)
print(avg_acc)
print(avg_acc_mean)

result_dict_all = OrderedDict()
result_dict_mean = OrderedDict()
result_dict_steps_avg_acc = OrderedDict()
result_dict_steps_last_acc = OrderedDict()

result_dict_all[f"model_name"] = "dytox"
result_dict_mean[f"model_name"] = "dytox"
result_dict_steps_avg_acc[f"model_name"] = "dytox"
result_dict_steps_last_acc[f"model_name"] = "dytox"

for i in range(len(avg_acc)):
    result_dict_all[f"avg_acc_{i + 1}"] = avg_acc[i]
    result_dict_steps_avg_acc[f"avg_acc_{i + 1}"] = avg_acc[i]
result_dict_all["avg_acc_mean"] = avg_acc_mean
result_dict_mean["avg_acc_mean"] = avg_acc_mean

for i in range(len(last_acc)):
    result_dict_all[f"last_acc_{i + 1}"] = last_acc[i]
    result_dict_steps_last_acc[f"last_acc_{i + 1}"] = last_acc[i]
result_dict_all["last_acc_mean"] = last_acc_mean
result_dict_mean["last_acc_mean"] = last_acc_mean

# 使用 ExcelWriter 同时写入多个 sheet
df_all = pd.DataFrame([result_dict_all])
df_mean = pd.DataFrame([result_dict_mean])
df_steps_avg_acc = pd.DataFrame([result_dict_steps_avg_acc])
df_steps_last_acc = pd.DataFrame([result_dict_steps_last_acc])

with pd.ExcelWriter('final_results_dytox.xlsx', engine='openpyxl') as writer:
    df_all.to_excel(writer, sheet_name='Results all', index=False)
    df_mean.to_excel(writer, sheet_name='Results mean', index=False)
    df_steps_avg_acc.to_excel(writer, sheet_name='Results steps avg acc', index=False)
    df_steps_last_acc.to_excel(writer, sheet_name='Results steps last acc', index=False)

print("All sheets:")
print(df_all)
print("\nMean results:")
print(df_mean)
print("\nSteps:")
print(df_steps_avg_acc)
print(df_steps_last_acc)