import pandas as pd
import matplotlib.pyplot as plt
import numpy as npy
import csv

# plt.rc("font", family="DengXian")  # 解决中文乱码
# plt.rcParams["axes.unicode_minus"] = False  # 符号报错

xlsx_file = 'data_analysis.xlsx'
df = pd.read_excel(xlsx_file)

csv_file = 'data_analysis.csv'
df.to_csv(csv_file, index=False)

# data = pd.read_csv(open('data_analysis.csv', encoding='utf-8'))

line_number1 = 0
line_number2 = 3
with open('data_analysis.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # 跳过前line_number行
    for _ in range(line_number1):
        # 将会跳过指定数量的行
        next(reader)
    # 读取第line_number行
    row1 = next(reader)

    for _ in range(line_number2):
        # 将会跳过指定数量的行
        next(reader)
    # 读取第line_number行
    row2 = next(reader)

label = row1[1:-1]
num = row2[1:-1]
# print(label, len(label))
# print(num, len(num))

exp = npy.arange(0, 0.2, 0.2/len(label))
plt.figure(figsize=(9, 9), dpi=120)
plt.pie(num, explode=exp, labels=label, autopct='%1.3f%%', shadow=True, startangle=90)

plt.show()