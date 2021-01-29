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
from get_historical_prices import *



class Chart:

    def __init__(self, symbol, startDate, endDate, granularity):
        self.symbol = symbol
        self.begin = datetime.strptime(startDate, '%Y-%m-%d')
        self.end = datetime.strptime(startDate, '%Y-%m-%d')
        self.granularity = granularity
        self.ticker = yf.Ticker(symbol)
        self.priceHistory = self.ticker.history(interval = granularity, \
                start = startDate, end = endDate)
    
    def _show_standard_poor(self):
        pass
    
    def _show_averages(self):
        pass

    def show_candlestick(self, showAverages = True, showRegression = False):

        mpl.rcParams['xtick.major.size'] = 0
        mpl.rcParams['xtick.major.pad'] = 10
        mpl.rcParams['ytick.major.size'] = 0
        mpl.rcParams['ytick.major.pad'] = 10

        #create figure
        fig = plt.figure(figsize = (10,5), facecolor = 'white')
        gs = mpl.gridspec.GridSpec(2,1, height_ratios = [3,1])
        ax_price = fig.add_subplot(gs[0])
        maxPrice = np.max(self.priceHistory['High'])
        minPrice = np.min(self.priceHistory['Low'])
        periodLength = self.priceHistory['Close'].shape[0]
        ax_price.grid(linestyle = '--', linewidth = 0.2, color = 'black', zorder = 0)
        ax_price.set(xlim = (0, periodLength), ylim = (minPrice*0.90, maxPrice*1.1))

        #draw candlestick plot
        ax_price = plot_candlestick(self.priceHistory, ax_price)

        #configure candlestick plot
        if(periodLength > 365):
            ax_price.set_xticks(range(0, self.priceHistory['Low'].shape[0],14))
        else:
            ax_price.set_xticks(range(0, self.priceHistory['Low'].shape[0],7))

        #format axis labels
        formatter = mpl.ticker.FormatStrFormatter('$%.2f')
        x_price.yaxis.set_major_formatter(formatter)
        ax_price.tick_params(labelbottom=False)
        ax_price.set_ylabel('Price')
        ax_price.yaxis.set_label_position('right')
        ax_price.yaxis.tick_right()

        #create volume plot
        maxVolume = np.max(self.priceHistory['Volume'])
        ax_volume = fig.add_subplot(gs[1], sharex = ax_price)
        ax_volume.set(xlim = (-1, timeFrameLength ), ylim = (0.0, maxVolume))

        #get moving average and relative strength information
        averages = get_moving_averages(historyForAverages)

        #draw volume plot
        ax_volume = plot_volume(self.priceHistory, ax_volume)

        #configure volume plot
        if(periodLength > 365):
            ax_volume.set_xticklabels(list(self.priceHistory.index.strftime('%m-%d-%Y'))[::14])
        else:
            ax_volume.set_xticklabels(list(self.priceHistory.index.strftime('%m-%d'))[::7])
        plt.xticks(rotation = 50)
        ax_volume.yaxis.tick_right()
        ax_volume.yaxis.set_label_position('right')
        ax_volume.set_ylabel('Shares')

        plt.show()
        
        return fig 
    

        
 

if __name__ == '__main__':
    c = Chart('NVDA', '2020-11-01', '2020-12-01', '1d')
    c.show_candlestick()
