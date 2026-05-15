import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Stock Market Analysis Dashboard",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("📈 Data-Driven Stock Analysis Dashboard")
st.markdown("### Time Series Forecasting and Portfolio Analysis using StockGro")

st.markdown("---")

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------
st.header("📌 Project Overview")

st.write(
    """
This dashboard presents a complete stock market analysis workflow using:

- ARIMA Forecasting
- Facebook Prophet
- LSTM Neural Network
- Volatility Analysis
- Portfolio Construction
- Live Trading Evaluation using StockGro

The project focuses on forecasting stock prices, constructing a diversified portfolio,
and comparing predicted market behavior with actual outcomes.
"""
)

# --------------------------------------------------
# STOCK SELECTION
# --------------------------------------------------
st.header("🏢 Selected Stocks")

stocks_df = pd.DataFrame({
    "Stock": [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ],
    "Sector": [
        "Energy",
        "IT",
        "Banking",
        "Metals",
        "Pharma"
    ]
})

st.dataframe(stocks_df, use_container_width=True)

# --------------------------------------------------
# MODEL COMPARISON
# --------------------------------------------------
st.header("📊 Model Evaluation")

model_df = pd.DataFrame({
    "Stock": [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ],
    "ARIMA_MAPE": [0.0494, 0.0538, 0.0147, 0.0517, 0.0328],
    "ARIMA_RMSE": [80.4558, 93.2729, 19.9018, 10.9796, 68.6894],
    "Prophet_MAPE": [0.1086, 0.0922, 0.0237, 0.1733, 0.0838],
    "Prophet_RMSE": [194.4516, 155.9325, 27.4764, 31.0868, 153.0439],
    "LSTM_MAPE": [0.0164, np.nan, np.nan, np.nan, np.nan],
    "LSTM_RMSE": [30.2821, np.nan, np.nan, np.nan, np.nan]
})

st.dataframe(model_df, use_container_width=True)

# --------------------------------------------------
# PORTFOLIO ALLOCATION
# --------------------------------------------------
st.header("💰 Portfolio Allocation")

allocation_df = pd.DataFrame({
    "Stock": [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ],
    "Allocation": [240000, 200000, 280000, 120000, 160000]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Allocation Table")
    st.dataframe(allocation_df, use_container_width=True)

with col2:
    st.subheader("Portfolio Allocation Chart")

    fig1, ax1 = plt.subplots(figsize=(6, 6))
    ax1.pie(
        allocation_df["Allocation"],
        labels=allocation_df["Stock"],
        autopct='%1.1f%%'
    )
    st.pyplot(fig1)

# --------------------------------------------------
# FORECAST VISUALIZATION
# --------------------------------------------------
st.header("📈 Forecast Visualization")

selected_stock = st.selectbox(
    "Select Stock",
    [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ]
)

# Dummy example data
actual = [100, 105, 108, 110, 112, 115]
predicted = [101, 104, 107, 111, 113, 116]

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.plot(actual, label="Actual")
ax2.plot(predicted, label="Predicted")
ax2.set_title(f"Actual vs Predicted Prices - {selected_stock}")
ax2.set_xlabel("Time")
ax2.set_ylabel("Price")
ax2.legend()

st.pyplot(fig2)

# --------------------------------------------------
# VOLATILITY ANALYSIS
# --------------------------------------------------
st.header("🌊 Volatility Analysis")

volatility = [2.1, 1.4, 0.9, 2.8, 1.7]

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.bar(
    [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ],
    volatility
)

ax3.set_title("Volatility Comparison")
ax3.set_ylabel("Volatility")

st.pyplot(fig3)

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------
st.header("🔥 Correlation Heatmap")

correlation_data = pd.DataFrame(
    {
        "Reliance": [1.00, 0.62, 0.55, 0.48, 0.51],
        "Infosys": [0.62, 1.00, 0.44, 0.39, 0.41],
        "HDFC Bank": [0.55, 0.44, 1.00, 0.36, 0.47],
        "Tata Steel": [0.48, 0.39, 0.36, 1.00, 0.33],
        "Sun Pharma": [0.51, 0.41, 0.47, 0.33, 1.00]
    },
    index=[
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ]
)

fig_heat, ax_heat = plt.subplots(figsize=(8, 6))

heatmap = ax_heat.imshow(correlation_data, aspect='auto')

ax_heat.set_xticks(range(len(correlation_data.columns)))
ax_heat.set_yticks(range(len(correlation_data.index)))

ax_heat.set_xticklabels(correlation_data.columns, rotation=45)
ax_heat.set_yticklabels(correlation_data.index)

for i in range(len(correlation_data.index)):
    for j in range(len(correlation_data.columns)):
        ax_heat.text(
            j,
            i,
            f"{correlation_data.iloc[i, j]:.2f}",
            ha='center',
            va='center'
        )

plt.colorbar(heatmap)

ax_heat.set_title("Stock Correlation Matrix")

st.pyplot(fig_heat)
# --------------------------------------------------
st.header("📉 Live Trading Performance")

final_df = pd.DataFrame({
    "Stock": [
        "Tata Steel",
        "HDFC Bank",
        "Infosys",
        "Sun Pharma",
        "Reliance"
    ],
    "Final Return %": [1.63, -0.16, -0.36, -2.99, -2.52]
})

st.dataframe(final_df, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.metric(
        label="Final Portfolio Return",
        value="-1.10%"
    )

with col4:
    st.metric(
        label="Final Portfolio Value",
        value="₹9,87,409.88"
    )

# --------------------------------------------------
# PREDICTED VS ACTUAL
# --------------------------------------------------
st.header("🔍 Predicted vs Actual Comparison")

comparison_df = pd.DataFrame({
    "Stock": [
        "Reliance",
        "Infosys",
        "HDFC Bank",
        "Tata Steel",
        "Sun Pharma"
    ],
    "Predicted_Day2": [1360, 1130, 748, 216, 1825],
    "Actual_Day2": [1338.11, 1115.42, 743.37, 216.77, 1810.54]
})

comparison_df["Error_%"] = abs(
    (
        comparison_df["Actual_Day2"]
        -
        comparison_df["Predicted_Day2"]
    )
    /
    comparison_df["Actual_Day2"]
) * 100

st.dataframe(comparison_df, use_container_width=True)

# --------------------------------------------------
# REFLECTIONS
# --------------------------------------------------
st.header("🧠 Key Learnings")

st.write(
    """
### Major Observations

- Diversification reduced overall portfolio risk.
- ARIMA produced stable forecasting performance.
- LSTM achieved strong results for Reliance.
- Real market movement was influenced by volatility and sector sentiment.
- Short-term market forecasting remains probabilistic.

### Future Improvements

- Add ensemble learning models
- Use sentiment analysis
- Add real-time stock APIs
- Deploy dashboard online
"""
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
