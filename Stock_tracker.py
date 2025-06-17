import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Define the stocks
stocks = {
    "S&P 500": "^GSPC",
    "Tesla": "TSLA"
}

def plot_stock_data(symbol, name):
    # Download last 30 days of historical data
    data = yf.download(symbol, period="30d")

    if data.empty:
        print(f"No data available for {name}.")
        return

    # Plot closing prices
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', linewidth=2)

    plt.title(f"{name} Stock Price - Last 30 Days")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.xticks(rotation=45)

    # Save or show the plot
    plt.show()

def main():
    for name, symbol in stocks.items():
        print(f"Plotting {name} ({symbol})...")
        plot_stock_data(symbol, name)

if __name__ == "__main__":
    main()
