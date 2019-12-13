import json
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import datetime
from statsmodels.stats.power import zt_ind_solve_power

def clean_asset_data(symbol):
    '''
    Function to gather API data from alphavantage.co into operable Pandas DataFrame. Converts string type objects into floats.
    
    Input: Asset's ticker symbol (type = String)

    Output: DataFrame with necessary data columnns for hypothesis testing, including Daily % change of the respective asset
    '''
    
    alpha_key = 'Y8YQFOIVHPA381U4'
    function = 'TIME_SERIES_DAILY'
    index_symbol = symbol
    url = f"https://www.alphavantage.co/query?function={function}&symbol={index_symbol}&outputsize=full&apikey={alpha_key}"
    response = requests.get(url)
    file = response.json()
    
    file_values = file['Time Series (Daily)']
    df = pd.DataFrame(file_values)
    asset_df = df.T
    asset_df.reset_index(inplace = True)
    column_head = [ 'date', 'open', 'high', 'low', 'close', 'volume']
    asset_df.columns = column_head
    
    asset_df['open'] = asset_df.open.astype(float)
    asset_df['high'] = asset_df.high.astype(float)
    asset_df['low'] = asset_df.low.astype(float)
    asset_df['close'] = asset_df.close.astype(float)
    asset_df['volume'] = asset_df.volume.astype(float)
    
    asset_df['day_pct_change'] = ((asset_df['close'] - asset_df['open'])/asset_df['open']) * 100
    
    for entry in asset_df:
        pct_change = (asset_df['close'] - asset_df['open'].iloc[-1])/asset_df['open'].iloc[-1]
        asset_df['overall_pct_change'] = pct_change * 100
    
    
    return asset_df