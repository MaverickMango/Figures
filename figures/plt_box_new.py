import sys
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import argparse


if __name__ == '__main__':

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    dataset_network_list = ['mnist_lenet1', 'mnist_lenet4',
                            'mnist_lenet5', 'cifar10_vgg16', 'cifar10_resnet20']
    # dataset_network_list = ['mnist_lenet1', 'mnist_lenet4']
    idx = 1
    fig=plt.figure(figsize=(20, 8))
    # gs = gridspec.GridSpec(1, 4)
    # gs.update(top=0.95, bottom=0.1, left=0.05, right=0.95, wspace=0.3, hspace=0.5)
    plt.subplots_adjust(top=0.95, bottom=0.15, left=0.04,
                        right=0.99, wspace=0.15, hspace=0.05)
    labels = ["SMS", 'SimpleDMS', "DMS"]
    colors = ['skyblue', 'darkturquoise', 'steelblue']
    xticks_font = 15
    ylabel_font = 15

    for key in dataset_network_list:

        dataset, network = key.split('_')[0], key.split('_')[1]

        plt.subplot(2, 5, idx)

        data = np.array(
                (pd.read_csv(f'fault/{dataset}_{network}_fault.csv')))[:, 1:-1]     
        data_nature = [data[11], data[12], data[13]]
        data_cw = [data[25], data[26], data[27]]
        data_bim = [data[39], data[40], data[41]]
        data_jsma = [data[67], data[68], data[69]]
        data_fgsm = [data[53], data[54], data[55]]


        # 绘制箱型图
        left = 0.5
        # patch_artist=True-->箱型可以更换颜色，positions=(1,1.4,1.8)-->将同一组的三个箱间隔设置为0.4，widths=0.3-->每个箱宽度为0.3
        bplot = plt.boxplot(data_nature, patch_artist=True, positions=(
            left, left + 0.4, left + 0.8), widths=0.3)
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        bplot2 = plt.boxplot(data_cw, patch_artist=True, positions=(
            left + 1.4, left + 1.8, left + 2.2), widths=0.3)
        for patch, color in zip(bplot2['boxes'], colors):
            patch.set_facecolor(color)

        bplot3 = plt.boxplot(data_bim, patch_artist=True, positions=(
            left + 2.8, left + 3.2, left + 3.6), widths=0.3)
        for patch, color in zip(bplot3['boxes'], colors):
            patch.set_facecolor(color)

        bplot4 = plt.boxplot(data_jsma, patch_artist=True, positions=(
            left + 4.2, left + 4.6, left + 5), widths=0.3)
        for patch, color in zip(bplot4['boxes'], colors):
            patch.set_facecolor(color)

        bplot5 = plt.boxplot(data_fgsm, patch_artist=True, positions=(
            left + 5.6, left + 6, left + 6.4), widths=0.3)
        for patch, color in zip(bplot5['boxes'], colors):
            patch.set_facecolor(color)


        x_position = [left, left + 1.4, left + 2.8, left + 4.2, left + 5.6]
        x_position_fmt = ["", "", "", "", ""]
        plt.xticks([i + 0.8 / 2 for i in x_position], x_position_fmt, fontsize=xticks_font)
        # plt.xlabel('候选集种类', fontsize=ylabel_font)
        plt.grid(linestyle="--", alpha=0.3)  # 绘制图中虚线 透明度0.3
        plt.title(key, fontsize=ylabel_font)
        if idx == 1 :
            plt.ylabel('Fault_rate (%)', fontsize=15)
        idx += 1


    for key in dataset_network_list:

        dataset, network = key.split('_')[0], key.split('_')[1]

        plt.subplot(2, 5, idx)

        data = np.array(
                (pd.read_csv(f'diversity/{dataset}_{network}_diversity.csv')))[:, 1:-1]
        data_nature = [data[11], data[12], data[13]]
        data_cw = [data[25], data[26], data[27]]
        data_bim = [data[39], data[40], data[41]]
        data_jsma = [data[67], data[68], data[69]]
        data_fgsm = [data[53], data[54], data[55]]


        # 绘制箱型图
        left = 0.5
        plt.subplot(2, 5, idx)
        # patch_artist=True-->箱型可以更换颜色，positions=(1,1.4,1.8)-->将同一组的三个箱间隔设置为0.4，widths=0.3-->每个箱宽度为0.3
        bplot = plt.boxplot(data_nature, patch_artist=True, labels=labels, positions=(
            left, left + 0.4, left + 0.8), widths=0.3)
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        bplot2 = plt.boxplot(data_cw, patch_artist=True, labels=labels, positions=(
            left + 1.4, left + 1.8, left + 2.2), widths=0.3)
        for patch, color in zip(bplot2['boxes'], colors):
            patch.set_facecolor(color)

        bplot3 = plt.boxplot(data_bim, patch_artist=True, labels=labels, positions=(
            left + 2.8, left + 3.2, left + 3.6), widths=0.3)
        for patch, color in zip(bplot3['boxes'], colors):
            patch.set_facecolor(color)

        bplot4 = plt.boxplot(data_jsma, patch_artist=True, labels=labels, positions=(
            left + 4.2, left + 4.6, left + 5), widths=0.3)
        for patch, color in zip(bplot4['boxes'], colors):
            patch.set_facecolor(color)

        bplot5 = plt.boxplot(data_fgsm, patch_artist=True, labels=labels, positions=(
            left + 5.6, left + 6, left + 6.4), widths=0.3)
        for patch, color in zip(bplot5['boxes'], colors):
            patch.set_facecolor(color)

        x_position = [left, left + 1.4, left + 2.8, left + 4.2, left + 5.6]
        x_position_fmt = ["Origin", "+CW", "+BIM", "+JSMA", '+FGSM']
        plt.xticks([i + 0.8 / 2 for i in x_position], x_position_fmt, fontsize=xticks_font)
        plt.xlabel('候选集种类', fontsize=ylabel_font)
        plt.grid(linestyle="--", alpha=0.3)  # 绘制图中虚线 透明度0.3
        # plt.title(key, fontsize=ylabel_font)
        if idx == 6 :
            plt.ylabel('Fault_type', fontsize=15)
        # plt.legend(bplot['boxes'], labels, loc='upper left',
        #            framealpha=0.3, prop = {'size':12})  # 绘制表示框，右下角绘制
        idx += 1

    plt.legend(bplot['boxes'], labels,bbox_to_anchor=(-1.15,-0.16), loc=1, ncol=3, prop = {'size':14})  # 绘制表示框，右下角绘制
    # plt.show()
    fig.savefig('v1.png', dpi=600, bbox_inches = 'tight')