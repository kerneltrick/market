import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

COLOR_DOWN = 'red'
COLOR_UP = 'green'

def plot_box(ax, dayNum, height, color):
    rect = mpl.patches.Rectangle(xy = (dayNum - 0.2, 0),
            width = 0.4,
            height = height,
            facecolor = color,
            edgecolor = 'black')
    ax.add_patch(rect)

    return rect

def plot_volume(priceHistory, ax):

    volume = priceHistory['Volume']
    for i in range(volume.shape[0]):
        if (priceHistory['Open'][i] > priceHistory['Close'][i]):
            color = COLOR_DOWN
        else:
            color = COLOR_UP
        plot_box(ax, i, volume[i], color)
        

    return ax
