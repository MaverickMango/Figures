import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('/Users/yangchen/Desktop/data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        h = line.split(',')
        c = []
        for i in h:
            c.append(float(i))
        print(np.mean(c))

labels = 'failing', 'passing'

all_data = []
max_len = 0
with open('/Users/yangchen/Desktop/data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        h = line.split(',')
        c = []
        for i in h:
            c.append(float(i))
        max_len = len(c) if len(c) > max_len else max_len
        for i in range(len(c), max_len):
            c.append(np.mean(c))
        all_data.append(c)
        # all_data.append(np.array(c).T)

# A = [0.4978, 0.5764, 0.5073, 0.5609]
# B = [0.5996, 0.65, 0.6251, 0.6473]
# C = [0.6015, 0.687, 0.6237, 0.6761]
# D = [0.5918, 0.6999, 0.6343, 0.6947]
# E = [0.577, 0.6932, 0.6593, 0.7036]
# F = [0.5637, 0.7161, 0.6683, 0.697]
plt.grid(True)  # 显示网格
plt.boxplot(all_data,
            medianprops={'color': 'red', 'linewidth': '1.5'},
            meanline=True,
            showmeans=True,
            meanprops={'color': 'blue', 'ls': '--', 'linewidth': '1.5'},
            flierprops={"marker": "o", "markerfacecolor": "red", "markersize": 10},
            labels=labels)
# plt.yticks(np.arange(0.4, 0.81, 0.1))
plt.show()
