import pandas as pd

def clean_data(df):
    df = df.rename(columns={
        'Open Price': 'Open',
        'High Price': 'High',
        'Low Price': 'Low',
        'Close Price': 'Close',
        'Total Traded Quantity': 'Volume'
    })

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)

    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df = df.dropna()

    return df