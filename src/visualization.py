import plotly.graph_objs as go

def plot_price(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Close'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA10'], name='MA10'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], name='MA50'))

    return fig


def plot_volume(df):
    fig = go.Figure()

    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'))

    return fig

def plot_grouped(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'],
        name='Avg Close'
    ))

    fig.add_trace(go.Bar(
        x=df.index,
        y=df['Volume'],
        name='Total Volume'
    ))

    return fig