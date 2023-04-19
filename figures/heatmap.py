import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# Create two lists of random values
tvm = [433,
167,
22,
11,
27,
26]

glow = [137,
56,
2,
1,
19,
15]

nGraph = [66,
40,
3,
0,
23,
8]

akg = [46,
26,
8,
3,
0,
6]

# tvm - glow
# 0.99
# 0.94 ngraph
# 0.97 akg

# glow-ngraph 0.96
# glow-akg 0.95

# 0.90 ngraph-akg
print(scipy.stats.pearsonr(tvm, glow)[0])

fig = plt.figure()
s = pd.DataFrame([
                [1,1, 1, 1],
                [0.99, 1, 1, 1],
                [0.94, 0.96, 1, 1],
                [0.97, 0.95, 0.90, 1]])
s.index=['TVM', 'Glow', 'nGraph', 'akg']
s.columns = ['TVM', 'Glow', 'nGraph', 'akg']

mask =  np.array([[False, True, True, True],
[False, False, True, True],
[False, False, False, True],
[False, False, False, False]])

with sns.axes_style("white"):
    sns_plot = sns.heatmap(s, square=True, annot=True,annot_kws={'weight':'bold'},cmap='YlGnBu', xticklabels =True, yticklabels=True,mask=mask)
    sns_plot.tick_params(labelsize=12)
    plt.show()