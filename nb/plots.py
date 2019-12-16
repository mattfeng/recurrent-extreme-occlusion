#!/usr/bin/env python

import matplotlib.pyplot as plt

SMALL_SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

cornet_z_top1_avg_acc = [0.39, 0.38, 0.39, 0.25, 0.25, 0.25, 0.18, 0.15, 0.17]
cornet_z_top5_avg_acc = [0.73, 0.74, 0.75, 0.54, 0.54, 0.54, 0.41, 0.36, 0.39]
cornet_r_top1_avg_acc = [0.37, 0.35, 0.37, 0.22, 0.23, 0.22, 0.16, 0.12, 0.15]
cornet_r_top5_avg_acc = [0.72, 0.72, 0.74, 0.47, 0.51, 0.49, 0.34, 0.30, 0.35]
cornet_s_top1_avg_acc = [0.53, 0.52, 0.53, 0.33, 0.34, 0.33, 0.22, 0.18, 0.23]
cornet_s_top5_avg_acc = [0.86, 0.85, 0.87, 0.63, 0.64, 0.61, 0.45, 0.40, 0.46]


def get_style(key):
    key = key.lower()
    if key == 'z':
        return 's', '#007EA7'
    elif key == 'r':
        return 'o', '#33658A'
    elif key == 's':
        return '^', '#002A32'

def plot_accuracy_over_difficulty(ax):
    top1 = [
        (cornet_z_top1_avg_acc, 'Z'),
        (cornet_r_top1_avg_acc, 'R'),
        (cornet_s_top1_avg_acc, 'S')
        ]

    top5 = [
        (cornet_z_top5_avg_acc, 'Z'),
        (cornet_r_top5_avg_acc, 'R'),
        (cornet_s_top5_avg_acc, 'S')
        ]

    ax.set_title('Accuracy vs. Occlusion Level', fontsize = 24)
    ax.set_xlabel('Occlusion level/difficulty')
    ax.set_ylabel('Average accuracy')
    ax.set_ylim([-0.05, 1.05])

    difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for acc, key in top1:
        marker, color = get_style(key)
        ax.plot(
            difficulty,
            acc,
            marker = marker,
            color = color,
            label = f'CORnet-{key} (top 1)'
            )

    for acc, key in top5:
        marker, color = get_style(key)
        ax.plot(
            difficulty,
            acc,
            marker = marker,
            color = color,
            linestyle = '--',
            label = f'CORnet-{key} (top 5)'
            )

    ax.legend()

