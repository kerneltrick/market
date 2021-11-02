import numpy as np
import matplotlib.pyplot as plt

def get_moving_averages(historyForAverages):
    
    closes = historyForAverages['Close']
    standardPoor = historyForAverages['standardPoor']
    volume = historyForAverages['Volume']
    observationSize = closes.shape[0]
    windowSize = observationSize - 200 

    averages = {'21-day': np.zeros(windowSize), 
            '50-day': np.zeros(windowSize), 
            '200-day': np.zeros(windowSize),
            'rs': np.zeros(windowSize),
            'volume-50-day': np.zeros(windowSize),
            'volume-200-day': np.zeros(windowSize)}

    for i in range(windowSize):
        averages['21-day'][i] = np.mean(closes[179+i:200+i])
        averages['50-day'][i] = np.mean(closes[150+i:200+i]) 
        averages['200-day'][i] = np.mean(closes[i:200+i])
        averages['rs'][i] = (closes[200+i] / standardPoor[i])
        averages['volume-50-day'][i] = np.mean(volume[150 + i: 200 + i])
        averages['volume-200-day'][i] = np.mean(volume[i:200+i])

    return averages


    
    
