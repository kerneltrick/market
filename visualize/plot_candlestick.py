import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

COLOR_DOWN = 'green'
COLOR_UP = 'red'

def plot_box(ax, dayNum, lower, height, color):
    rect = mpl.patches.Rectangle(xy = (dayNum - 0.2, lower), 
            width = 0.4,
            height = height,
            facecolor = color,
            edgecolor = color,
            alpha=0.8)
    ax.add_patch(rect)
    
    return rect

def plot_wick(ax, dayNum, low, high):
    line = mpl.lines.Line2D(xdata = (dayNum, dayNum), ydata = (low, high), linewidth = 1.0, antialiased = True)
    ax.add_line(line)

    return line

def plot_candlestick(priceHistory, ax):
 
    wicks = []
    boxes = []
    for i in range(priceHistory['Low'].shape[0]):
        low = priceHistory['Low'][i]
        high = priceHistory['High'][i]
        openPrice = priceHistory['Open'][i]
        closePrice = priceHistory['Close'][i]
        day = list(priceHistory.index.strftime('%Y-%m-%d'))[i]
        
        height = 0
        wicks.append(plot_wick(ax, i, low, high))
        if openPrice > closePrice:
            color = COLOR_UP
            height = openPrice - closePrice
            lower = closePrice
        else:
            color = COLOR_DOWN
            height = closePrice - openPrice
            lower = openPrice
        boxes.append(plot_box(ax, i, lower, height, color))
        ax.autoscale_view()

    return ax
    
       

