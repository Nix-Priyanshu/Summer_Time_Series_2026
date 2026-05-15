# Data-Driven Stock Analysis using Time Series Models on StockGro

## Time Series Analysis 2026 Capstone Project

### Submitted By

* Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
* Institute/College: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
* Course: Time Series Analysis 2026

\---

# 1\. Introduction

This capstone project focuses on applying time series forecasting techniques for stock market analysis and portfolio construction using the StockGro virtual trading platform. The project integrates quantitative analysis, forecasting models, volatility estimation, and portfolio allocation strategies to simulate a real-world investment workflow.

The objective of the project was to:

* Analyze historical NSE stock data
* Build forecasting models using ARIMA, Prophet, and LSTM
* Estimate volatility and trend behavior
* Construct a diversified virtual portfolio of ₹10,00,000
* Execute the strategy live on StockGro
* Compare model predictions with actual market outcomes

The project combines data science, financial forecasting, and portfolio management concepts in a practical market simulation environment.

\---

# 2\. Stock Universe Selection

To ensure diversification across multiple sectors, five NSE-listed stocks were selected from different industries.

|Stock|Sector|Reason for Selection|
|-|-|-|
|Reliance Industries|Energy \& Conglomerate|Large-cap stock with strong market influence and stable historical trend|
|Infosys|Information Technology|High liquidity and strong sector momentum in IT|
|HDFC Bank|Banking|Stable banking stock with moderate volatility|
|Tata Steel|Metals|Volatile stock useful for trend and volatility analysis|
|Sun Pharma|Pharmaceuticals|Defensive sector stock with consistent market presence|

### Selection Rationale

The stock selection was based on:

* Sector diversification
* Rolling volatility analysis
* Trend consistency from historical data
* Correlation balancing across sectors

This diversified approach helped reduce concentration risk and improved portfolio stability.

\---

# 3\. Dataset and Data Collection

## Data Source

Historical stock market data was collected using the Yahoo Finance API through the `yfinance` Python library.

## Dataset Specifications

|Parameter|Value|
|-|-|
|Source|Yahoo Finance|
|Time Period|Jan 2021 – Dec 2025|
|Interval|Daily (1 Day)|
|Market|NSE|

### Libraries Used

* pandas
* numpy
* matplotlib
* seaborn
* yfinance
* prophet
* tensorflow
* scikit-learn
* statsmodels

\---

# 4\. Data Preprocessing

Several preprocessing techniques were applied before building forecasting models.

## Preprocessing Steps

### 4.1 Handling Missing Values

Missing values were handled using forward filling and removal of invalid rows.

### 4.2 Stationarity Testing

The Augmented Dickey-Fuller (ADF) test was used to check stationarity.

### ADF Test Results

|Stock|Result|
|-|-|
|Reliance|Non-Stationary|
|Infosys|Non-Stationary|
|HDFC Bank|Non-Stationary|
|Tata Steel|Non-Stationary|
|Sun Pharma|Non-Stationary|

Differencing was applied where required to stabilize the mean and variance.

### 4.3 Train-Test Split

|Dataset|Period|
|-|-|
|Training Set|Jan 2021 – Jun 2025|
|Testing Set|Jul 2025 – Dec 2025|

### 4.4 Scaling

MinMaxScaler was used for LSTM preprocessing.

\---

# 5\. Forecasting Models

Three forecasting models were implemented:

1. ARIMA
2. Facebook Prophet
3. LSTM Neural Network

## 5.1 ARIMA Model

ARIMA was used for statistical time series forecasting. Model tuning was performed using AIC and BIC values.

### Advantages

* Interpretable
* Effective for linear trends
* Good statistical foundation

### Limitations

* Struggles with non-linear patterns
* Sensitive to parameter tuning

\---

## 5.2 Facebook Prophet

Prophet was used for trend and seasonality forecasting.

### Advantages

* Handles seasonality well
* Easy implementation
* Effective for business forecasting

### Limitations

* Lower short-term prediction accuracy in volatile markets

\---

## 5.3 LSTM Model

LSTM (Long Short-Term Memory) neural network was implemented for deep learning-based forecasting.

### Advantages

* Captures non-linear relationships
* Learns sequential dependencies
* Performs well on large datasets

### Limitations

* Computationally expensive
* Requires scaling and tuning

\---

# 6\. Model Evaluation and Comparison

The forecasting models were evaluated using:

* MAPE (Mean Absolute Percentage Error)
* RMSE (Root Mean Squared Error)
* Directional Accuracy

## Model Comparison Table

|Stock|ARIMA\_MAPE|ARIMA\_RMSE|Prophet\_MAPE|Prophet\_RMSE|LSTM\_MAPE|LSTM\_RMSE|
|-|-|-|-|-|-|-|
|Reliance|0.0494|80.4558|0.1086|194.4516|0.0164|30.2821|
|Infosys|0.0538|93.2729|0.0922|155.9325|-|-|
|HDFC Bank|0.0147|19.9018|0.0237|27.4764|-|-|
|Tata Steel|0.0517|10.9796|0.1733|31.0868|-|-|
|Sun Pharma|0.0328|68.6894|0.0838|153.0439|-|-|

## Observations

* LSTM achieved the best accuracy for Reliance.
* ARIMA produced more stable results compared to Prophet.
* Prophet captured trend behavior but struggled with short-term volatility.
* ARIMA was selected as the primary forecasting model due to consistency and interpretability.

\---

# 7\. Volatility and Trend Analysis

## Volatility Estimation

Log returns and rolling standard deviation were used to estimate stock volatility.

### Observations

* Tata Steel showed the highest volatility.
* HDFC Bank showed relatively stable movement.
* Reliance and Sun Pharma experienced moderate fluctuations.

## Trend Analysis

Seasonal decomposition was applied to analyze:

* Trend
* Seasonality
* Residual noise

### Findings

* Infosys showed relatively stable upward movement.
* Tata Steel displayed strong cyclical fluctuations.
* HDFC Bank remained comparatively stable.

\---

# 8\. Portfolio Construction and Allocation

The portfolio was constructed using:

* Forecast-Guided Allocation
* Volatility-Aware Sizing
* Sector Diversification

## Final Allocation Table

|Stock|Allocation (₹)|
|-|-|
|Reliance|240000|
|Infosys|200000|
|HDFC Bank|280000|
|Tata Steel|120000|
|Sun Pharma|160000|

## Allocation Strategy

Higher allocations were assigned to:

* relatively stable stocks,
* stocks with better forecast consistency,
* diversified sector exposure.

Volatile stocks received relatively smaller allocations.

\---

# 9\. StockGro Virtual Trading Execution

The portfolio was executed on the StockGro platform using the allocated virtual capital.

## Final Purchased Quantities

|Stock|Quantity|
|-|-|
|Reliance|173|
|Infosys|179|
|HDFC Bank|376|
|Tata Steel|563|
|Sun Pharma|86|

## Execution Notes

Minor allocation adjustments were made due to StockGro exposure constraints.

Screenshots of:

* portfolio execution,
* holdings,
* portfolio summary,
* and market observations

were recorded during the trading window.

\---

# 10\. Predicted vs Actual Market Performance

## Final Portfolio Results

|Metric|Value|
|-|-|
|Invested Value|₹9,98,395.83|
|Current Value|₹9,87,409.88|
|Overall Returns|-₹10,985.95 (-1.10%)|

## Final Stock-Wise Performance

|Stock|Final Return %|
|-|-|
|Tata Steel|+1.63%|
|HDFC Bank|-0.16%|
|Infosys|-0.36%|
|Sun Pharma|-2.99%|
|Reliance|-2.52%|

## Observations

* Tata Steel became the best-performing stock during the observation window.
* Reliance and Sun Pharma negatively affected portfolio performance.
* Diversification reduced the impact of losses from individual stocks.
* Market volatility and short-term sentiment influenced actual movement.

\---

# 11\. Reflections and Learnings

This project demonstrated the practical challenges of financial forecasting and portfolio management.

## Key Learnings

* Stock prices are highly volatile and influenced by multiple market factors.
* Time series models provide probabilistic guidance rather than guaranteed predictions.
* Diversification is important for reducing portfolio risk.
* ARIMA models provide stable and interpretable forecasts.
* Real market execution introduces practical constraints such as exposure limits and transaction costs.

## What Could Be Improved

* Use larger datasets and more advanced deep learning models.
* Incorporate sentiment analysis and macroeconomic indicators.
* Use ensemble forecasting for improved prediction accuracy.
* Develop a fully interactive dashboard for real-time monitoring.

\---

# 12\. Conclusion

This capstone successfully integrated time series forecasting, volatility analysis, and portfolio construction into a real-world stock market simulation environment.

The project demonstrated the application of:

* statistical forecasting,
* machine learning,
* risk management,
* and diversified portfolio allocation.

Although the final portfolio produced a small short-term loss, the project successfully achieved its primary objective of implementing a data-driven investment workflow and evaluating forecasting performance against real market behavior.

\---

# 13\. References

1. Yahoo Finance API Documentation
2. Prophet Documentation
3. TensorFlow Documentation
4. Statsmodels Documentation
5. StockGro Platform
6. NSE India Market Data

