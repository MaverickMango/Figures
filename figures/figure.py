import matplotlib.pyplot as plt

line_fast = [43.7, 45.1, 44.1, 42.7, 43.6, 50.8, 50.6]
line_java = [42, 43.2, 43.4, 42, 43.1, 50.6, 49.6]
line_seed = [35.4, 36.3, 36.8, 38, 40.7, 48.1, 48.1]
func_fast = [36, 36.9, 36.3, 35.5, 35.7, 41.5, 41]
func_java = [34.8, 35.7, 35.7, 34.5, 35.2, 41.3, 40.1]
func_seed = [29.3, 30.1, 30.2, 30.9, 33.4, 39.6, 38.9]
bran_fast = [32, 33.3, 32.4, 30.6, 32.2, 40.3, 39.5]
bran_java = [30.3, 31.6, 32, 30.2, 32.2, 39.8, 38.8]
bran_seed = [24.1, 24.9, 25.4, 26.9, 28.8, 36.4, 36.1]
for fast, java, seed, name in zip([line_fast, func_fast, bran_fast], [line_java, func_java, bran_java],
                                  [line_seed, func_seed, bran_seed], ["Line", "Function", "Branch"]):
    x = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
    ls = [fast, java, seed]
    types = ['Fasttailor', 'Javatailor', 'seed']
    line_style = ['-', '--', ':', '-.']
    markers = ['*', 's', '^', 'x']
    colors = [4, 4, 4, 4]

    plt.yticks(fontproperties='Times New Roman', weight='bold', fontsize=16)  # 设置大小及加粗
    plt.xticks(fontproperties='Times New Roman', weight='bold', fontsize=16)

    plt.xlabel('Benchmark', weight='bold', fontsize=16)
    plt.ylabel(name + ' Coverage', weight='bold', fontsize=16)
    plt.rc('legend', fontsize=16)

    for l, t, style, marker, c in zip(ls, types, line_style, markers, colors):
        plt.plot(x, l, label=t, ls=style, marker=marker, markersize=4)
        plt.legend()
    # plt.savefig('./' + name + '.png', dpi=300)
    plt.show()
