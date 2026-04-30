import pandas as pd

def clean_data(df):
    df = df.rename(columns={
        'Open Price': 'Open',
        'High Price': 'High',
        'Low Price': 'Low',
        'Close Price': 'Close',
        'Total Traded Quantity': 'Volume'
    })

    # 🔥 safer datetime conversion
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # ❗ remove invalid dates
    df = df.dropna(subset=['Date'])

    # sort properly
    df = df.sort_values('Date')

    # set index
    df.set_index('Date', inplace=True)

    # ensure numeric values (VERY IMPORTANT)
    df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[
        ['Open', 'High', 'Low', 'Close', 'Volume']
    ].apply(pd.to_numeric, errors='coerce')

    df = df.dropna()

    return df