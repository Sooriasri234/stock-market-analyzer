import numpy as np
import pandas as pd

def add_features(df):
    df['MA10'] = df['Close'].rolling(10).mean()
    df['MA50'] = df['Close'].rolling(50).mean()

    df['Daily Return'] = np.log(df['Close'] / df['Close'].shift(1))
    df['Volatility'] = df['Daily Return'].rolling(10).std()

    return df

def group_data(df, freq='M'):
    """
    freq options:
    'W' = Weekly
    'M' = Monthly
    'Q' = Quarterly
    'Y' = Yearly
    """

    grouped = df.resample(freq).agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'mean',
        'Volume': 'sum'
    })

    return grouped.dropna()