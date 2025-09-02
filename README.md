# Quantitative Portfolio Analysis Dashboard

A comprehensive Streamlit-based financial analytics dashboard that performs quantitative analysis on major technology stocks, calculating key risk metrics and performance indicators for informed investment decisions.

## 🚀 Features

### Real-Time Market Data Analysis
- **Live Stock Data**: Fetches real-time historical price data using Yahoo Finance API
- **Multi-Asset Analysis**: Simultaneous analysis of AAPL, GOOG, and MSFT stocks
- **Interactive Visualizations**: Dynamic line charts showing price movements and trends

### Risk & Performance Metrics
- **Daily Returns Calculation**: Computes percentage daily returns for each stock
- **Volatility Analysis**: Standard deviation calculations to measure price volatility
- **Sharpe Ratio**: Risk-adjusted return metrics for performance comparison
- **Comparative Analysis**: Side-by-side performance evaluation across assets

### Interactive Dashboard
- **Real-Time Refresh**: Manual data refresh capability for up-to-date analysis
- **Data Tables**: Detailed tabular view of historical price data and returns
- **Visual Charts**: Clean, intuitive line charts for trend analysis

## 📊 Technical Implementation

### Technologies Used
- **Python 3.x**: Core programming language
- **Streamlit**: Interactive web application framework
- **yfinance**: Yahoo Finance API for market data retrieval
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

### Key Calculations
- **Daily Returns**: `(Price_today - Price_yesterday) / Price_yesterday`
- **Average Returns**: Mean of daily returns over the period
- **Standard Deviation**: Risk measure showing price volatility
- **Sharpe Ratio**: `Average_Return / Standard_Deviation` (simplified version)

## 🛠️ Installation & Setup

### Prerequisites
```bash
pip install streamlit yfinance pandas numpy
```

### Running the Application
```bash
streamlit run "portfolio risk dashboard.py"
```

The dashboard will launch in your default web browser at `http://localhost:8501`

## 📈 Data Analysis Period

- **Time Frame**: January 1, 2020 - January 1, 2021
- **Assets Analyzed**: Apple (AAPL), Google (GOOG), Microsoft (MSFT)
- **Data Source**: Yahoo Finance

## 🔍 Key Insights Generated

1. **Risk Assessment**: Identifies which stocks have higher volatility
2. **Return Analysis**: Compares average daily returns across tech giants
3. **Risk-Adjusted Performance**: Sharpe ratios help identify best risk-adjusted returns
4. **Portfolio Diversification**: Data supports informed diversification decisions

## 🎯 Use Cases

- **Investment Research**: Fundamental analysis for stock selection
- **Risk Management**: Understanding volatility profiles of major tech stocks
- **Portfolio Construction**: Data-driven asset allocation decisions
- **Performance Benchmarking**: Comparative analysis of industry leaders

## 📋 Future Enhancements

- [ ] Add more stocks and sectors for broader analysis
- [ ] Implement portfolio optimization algorithms
- [ ] Include additional risk metrics (VaR, Beta, Alpha)
- [ ] Add Monte Carlo simulations for scenario analysis
- [ ] Integrate real-time news sentiment analysis

## 📊 Sample Output

The dashboard provides:
- Historical price charts for each stock
- Daily returns data and statistics
- Risk metrics (standard deviation)
- Performance ratios (Sharpe ratio)
- Comparative analysis results

## 🤝 Contributing

This project serves as a foundation for quantitative finance analysis. Contributions and suggestions for additional features are welcome.

## 📄 License

This project is open source and available for educational and research purposes.

---

**Note**: This dashboard is designed for educational and research purposes. Always consult with financial professionals before making investment decisions.