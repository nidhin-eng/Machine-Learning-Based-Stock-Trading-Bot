# Machine-Learning-Based-Stock-Trading-Bot

This project is an automated stock trading bot built using the LumiBot framework, which integrates with Alpaca’s brokerage API for real-time and historical trading. The bot leverages machine learning models to make buy/sell decisions based on market data.

Key Features:
ML-Powered Strategy: Uses a trained model (e.g., Random Forest, XGBoost) to predict stock price movements and execute trades.

Broker Integration: Connects with Alpaca's paper or live trading API to place real or simulated trades.

Backtesting: Simulates performance over historical data to validate strategy.

Real-Time Trading: Operates in live markets using Alpaca’s WebSocket streams.

Risk Management: Allocates a configurable portion of capital (cash_at_risk) per trade.

Tech Stack:
Python

LumiBot (for strategy logic and execution)

Alpaca API (broker connection)

scikit-learn / XGBoost (for ML models)

pandas / numpy / matplotlib (for data processing & visualization)
