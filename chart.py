import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
import sys
from datetime import datetime, timedelta
from plot_candlestick import plot_candlestick
from plot_volume import plot_volume
from get_moving_averages import *



class Chart:

    def __init__(self, symbol, startDate, endDate, granularity):
        self.symbol = symbol
        self.begin = datetime.strptime(startDate, '%Y-%m-%d')
        self.end = datetime.strptime(startDate, '%Y-%m-%d')
        self.granularity = granularity
        self.ticker = yf.Ticker(symbol)
        self.priceHistory = self.ticker.history(interval = granularity, \
                start = startDate, end = endDate)
        self.candlestick = self.make_candlestick()


    def make_candlestick(self):

        mpl.rcParams['xtick.major.size'] = 0
        mpl.rcParams['xtick.major.pad'] = 10
        mpl.rcParams['ytick.major.size'] = 0
        mpl.rcParams['ytick.major.pad'] = 10

        #create figure
        fig = plt.figure(figsize = (10,5), facecolor = 'white')
        gs = mpl.gridspec.GridSpec(2,1, height_ratios = [3,1])
        ax_price = fig.add_subplot(gs[0])

        return fig 
    

    def show_candlestick(self):
        self.candlestick.show()
        
 

if __name__ == '__main__':
    c = Chart('NVDA', '2020-11-01', '2020-12-01', '1d')
    c.show_candlestick()
