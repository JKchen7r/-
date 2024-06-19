import pandas as pd
import matplotlib.pyplot as plt
import numpy as npy
import csv

df = pd.read_csv('data_analysis.csv')

# 选择需要切分的列数据
label = df['q_type'][0:3]
num = df['num'][0:3]

# print(label)
# print(num)
# 切分列数据，这里以空格为分隔符，可以根据需要更改
plt.figure(figsize=(9, 9), dpi=120)

plt.pie(num, colors=plt.get_cmap('viridis')(npy.linspace(0.1, 0.7, 3)),
                    labels=label,autopct='%1.1f%%', pctdistance=0.85,
     )
# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)
# Adding Title of chart
plt.title('Question Type Details')

plt.show()