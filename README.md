# 📈 Python Stock Tracker

A simple Python app that tracks and visualizes the stock prices of popular stocks like **S&P 500** and **Tesla** using the `yfinance` and `matplotlib` libraries.

## 🔍 Features

- Fetches real-time and historical stock data using Yahoo Finance
- Tracks:
  - 🗂️ S&P 500 Index (`^GSPC`)
  - 🚗 Tesla (`TSLA`)
- Visualizes 30-day price trends using Matplotlib
- Displays current price, daily change, and percentage movement

## 🖥️ Demo

![Tesla Chart](./screenshots/tesla_chart.png)  
*(Example chart - Tesla 30-day close price)*

## 📦 Requirements

- Python 3.7+
- `yfinance`
- `matplotlib`

Install dependencies with:

pip install yfinance matplotlib

## 🚀 How to Run

1. Clone the repo:

git clone https://github.com/your-username/stock-tracker.git
cd stock-tracker

2. Run the tracker:

python stock_tracker.py

The script will display the current stock data and open charts in separate windows.

## 📊 Future Enhancements

- Add more stocks via a configuration file or command-line arguments

- Include moving averages (e.g. 7-day, 30-day)

- Build a web dashboard with Streamlit or Flask

- Schedule automatic tracking and save logs to CSV

## 📁 Project Structure

stock-tracker/

│

├── stock_tracker.py      # Main script

├── README.md             # Project readme

├── screenshots/          # Optional: chart images for GitHub preview

## 📜 License
This project is licensed under the MIT License.
