import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from get_historical_prices import *
from plot_candlestick import plot_candlestick
from plot_volume import plot_volume
from get_moving_averages import *
from cursor import *

def market(symbol, startDate, endDate, granularity):
   
    periodBegin = datetime.strptime(startDate, '%Y-%m-%d')
    preamble = periodBegin - timedelta(days = 365)
    standardPoor = get_historical_prices('^GSPC', startDate, endDate, granularity)
    priceHistory = get_historical_prices(symbol, startDate, endDate, granularity)
    preambleHistory = get_historical_prices(symbol, preamble, endDate, granularity)

    periodLength = priceHistory['Close'].shape[0]
    startPreamble = preambleHistory['Close'].shape[0] - (200 + periodLength)
    historyForAverages = {'Close': preambleHistory['Close'][startPreamble:], 'Volume': preambleHistory['Volume'][startPreamble:], 'standardPoor': standardPoor['Close']}

    maxPrice = np.max(priceHistory['High'])
    minPrice = np.min(priceHistory['Low'])
    timeFrameLength = priceHistory['High'].shape[0]

    #configure mpl backend
    mpl.rcParams['xtick.major.size'] = 0
    mpl.rcParams['xtick.major.pad'] = 10
    mpl.rcParams['ytick.major.size'] = 0
    mpl.rcParams['ytick.major.pad'] = 10
    
    #create figure
    fig = plt.figure(figsize = (10,5), facecolor = 'white')
    gs = mpl.gridspec.GridSpec(2,1, height_ratios = [3,1])

    #create candlestick plot
    ax_price = fig.add_subplot(gs[0])
    ax_price.grid(linestyle = '--', linewidth = 0.2, color = 'black', zorder = 0)
    ax_price.set(xlim = (0, timeFrameLength ), ylim = (minPrice*0.90, maxPrice*1.1))
    #draw candlestick plot
    ax_price = plot_candlestick(priceHistory, ax_price) 
    
    #configure candlestick plot
    if(periodLength > 365):
        ax_price.set_xticks(range(0, priceHistory['Low'].shape[0],14))
    else:
        ax_price.set_xticks(range(0, priceHistory['Low'].shape[0], 7))
    formatter = mpl.ticker.FormatStrFormatter('$%.2f')
    ax_price.yaxis.set_major_formatter(formatter)
    ax_price.tick_params(labelbottom=False)
    ax_price.set_ylabel('Price')
    ax_price.yaxis.set_label_position('right')
    ax_price.yaxis.tick_right()
    
    #Crosshair cursor
    blitted_cursor = Cursor(ax_price)
    fig.canvas.mpl_connect('motion_notify_event', blitted_cursor.on_mouse_move)


    #create volume plot
    maxVolume = np.max(priceHistory['Volume'])
    ax_volume = fig.add_subplot(gs[1], sharex = ax_price)
    ax_volume.set(xlim = (-1, timeFrameLength ), ylim = (0.0, maxVolume))
    
    #get moving average and relative strength information
    averages = get_moving_averages(historyForAverages)

    #draw volume plot
    ax_volume = plot_volume(priceHistory, ax_volume)

    #configure volume plot
    if(periodLength > 365):
        ax_volume.set_xticklabels(list(priceHistory.index.strftime('%m-%d-%Y'))[::14])
    else:
        ax_volume.set_xticklabels(list(priceHistory.index.strftime('%m-%d'))[::7])
    plt.xticks(rotation = 50)
    ax_volume.yaxis.tick_right()
    ax_volume.yaxis.set_label_position('right')
    ax_volume.set_ylabel('Shares')

    #Plot curves for moving averages
    time = np.arange(periodLength)
    ax_volume.plot(time, averages['volume-50-day'], color='red')
    ax_volume.plot(time, averages['volume-200-day'], color='black')
    ax_price.plot(time, averages['21-day'], color='blue', label='21-Day')
    ax_price.plot(time, averages['50-day'], color='red', label='50-Day')
    ax_price.plot(time, averages['200-day'], color='black', label='200-Day')
  

    #plot relative strength curve
    ax_rs = ax_price.twinx()
    ax_rs.plot(time, averages['rs'], color='green', label='RS')

    #configure relative strength axes
    maxRelativeStrength = max(averages['rs'])
    minRelativeStrength = min(averages['rs'])
    ax_rs.set(xlim = (0, timeFrameLength ), ylim = (minRelativeStrength*0.90, maxRelativeStrength*2.0))
    ax_rs.yaxis.set_ticklabels([])
    ax_rs.yaxis.tick_left()
    

    #Plot S&P
    ax_standardPoor = ax_price.twinx()
    ax_standardPoor.plot(time, standardPoor['Close'], label='S&P', color = 'grey')

    #Configure S&P
    maxSP = max(standardPoor['Close'])
    minSP = min(standardPoor['Close'])
    ax_standardPoor.set(xlim = (0, timeFrameLength ), ylim = (minSP*0.3, maxSP*1.05))
    ax_standardPoor.yaxis.set_ticklabels([])
    ax_rs.yaxis.tick_left()

    #symbol header and legend
    ax_price.plot(np.nan, color='green', label = 'RS' )
    ax_price.plot(np.nan, color='grey', label = 'S&P')
    ax_price.text(0,1.01, symbol, va = 'baseline', ha = 'left', size = 30, transform = ax_price.transAxes)  

    
    ax_price.legend(loc=0)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('usage: market.py symbol startDate endDate granularity')
        sys.exit(2)
    
    symbol = sys.argv[1]
    
    if len(sys.argv) == 5:
        startDate = sys.argv[2]
        endDate = sys.argv[3]
        granularity = sys.argv[4]
    elif len(sys.argv) >= 3:
        delta = int(sys.argv[2])
        endDate = datetime.today()
        startDate = endDate - timedelta(days=delta)
        startDate = startDate.strftime('%Y-%m-%d')
        endDate = endDate.strftime('%Y-%m-%d')
        granularity = '1d'
        if len(sys.argv) == 4:
            granularity = sys.argv[3]
    else:
        print('incorrect argument string')
        sys.exit(2)

    market(symbol, startDate, endDate, granularity)
