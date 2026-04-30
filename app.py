import streamlit as st
import pandas as pd

from src.preprocessing import clean_data
from src.analysis import add_features
from src.visualization import plot_price, plot_volume
from src.analysis import group_data
from src.visualization import plot_grouped

st.set_page_config(layout="wide")

st.title("📊 HCLTECH Stock Analyzer")

# Load data
df = pd.read_csv("data/HCL.csv")

# Process
df = clean_data(df)
df = add_features(df)

# Sidebar filters
st.sidebar.header("Filter Data")

start_date = st.sidebar.date_input("Start Date", df.index.min())
end_date = st.sidebar.date_input("End Date", df.index.max())

df_filtered = df.loc[start_date:end_date]

# Show data
st.subheader("Filtered Data")
st.write(df_filtered.tail())

# Charts
st.subheader("📈 Price Analysis")
st.plotly_chart(plot_price(df_filtered), use_container_width=True)

st.subheader("📊 Volume Analysis")
st.plotly_chart(plot_volume(df_filtered), use_container_width=True)

# Metrics
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Latest Price", round(df_filtered['Close'].iloc[-1], 2))
col2.metric("Avg Return", round(df_filtered['Daily Return'].mean(), 5))
col3.metric("Volatility", round(df_filtered['Volatility'].mean(), 5))

group_option = st.sidebar.selectbox(
    "Group Data By",
    ["Daily", "Weekly", "Monthly", "Yearly"]
)

freq_map = {
    "Daily": None,
    "Weekly": "W",
    "Monthly": "M",
    "Yearly": "Y"
}

if freq_map[group_option]:
    df_grouped = group_data(df, freq_map[group_option])
else:
    df_grouped = df.copy()

st.subheader(f"📊 {group_option} Aggregated Data")
st.write(df_grouped.tail())

st.plotly_chart(plot_grouped(df_grouped), use_container_width=True)