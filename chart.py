import numpy as np
import os
from datetime import datetime, timedelta


class Chart:

    def __init__(self, symbol, startDate, endDate):
        self.symbol = symbol
        self.begin = datetime.strptime(startDate, '%Y-%m-%d')
        self.end = datetime.strptime(startDate, '%Y-%m-%d')
        
 

