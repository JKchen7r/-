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

# expp = npy.arange(0.01, 0.01 * len(num) + 0.001, 0.01)
plt.figure(figsize=(9, 9), dpi=120)

plt.pie(num, colors=plt.get_cmap('viridis')(npy.linspace(0, 1, 15)),
                    labels=label,autopct='%1.1f%%', pctdistance=0.85,
     )
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)
# Adding Title of chart
plt.title('Chapter Title Details')

# piee, texts = plt.pie(num, colors=plt.get_cmap('viridis')(npy.linspace(0, 1, 15)),
#                       explode=expp, startangle=45, wedgeprops={'width': 0.3})
# plt.pie(num, explode=expp, colors=plt.get_cmap('viridis')(npy.linspace(0, 1, 15)),
#         radius=0.6, startangle=45, wedgeprops={'width': 0.03, 'alpha': 0.7})


# for i,p in enumerate(piee):
#     here = (p.theta2 - p.theta1) / 2.0 + p.theta1
#     label_y = npy.sin(here / 180 * npy.pi)
#     label_x = npy.cos(here / 180 * npy.pi)
#
#     connect = f"angle,angleA=0,angleB={here}"
#
#     align = {-1: "right", 1: "left"}[int(npy.sign(label_x))]
#     plt.annotate(label[i],
#                  xy=(label_x, label_y),
#                  xytext=((1.1 + i * 0.05) * npy.sign(label_x),
#                  (1.1 + i * 0.05) * label_y),
#                  fontsize=17, horizontalalignment=align, wight='bold', arrowprops=dict(arrowstyle='-', connectionstyle=connect),
#                  zorder=0, va='center')

plt.show()






