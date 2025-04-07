import requests

BASE_URL = "http://127.0.0.1:5000"  # Base URL of the Flask app

def get_all_stocks():
    """Fetch the list of all available stock tickers."""
    try:
        response = requests.get(f"{BASE_URL}/api/stocks")
        if response.status_code == 200:
            data = response.json()
            print("Available Stock Tickers:")
            for ticker in data.get('tickers', []):
                print(f"- {ticker}")
        else:
            print(f"Error: {response.status_code} - {response.json().get('error')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_stock_data(ticker, date=None):
    """Fetch stock data for a specific ticker, optionally filtered by date."""
    try:
        params = {'date': date} if date else {}
        response = requests.get(f"{BASE_URL}/api/stock/{ticker}", params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Stock Data for {ticker}:")
            print(data)
        else:
            print(f"Error: {response.status_code} - {response.json().get('error')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage of the APIs
    print("Fetching all stock tickers...")
    get_all_stocks()
    
    print("\nFetching stock data for a specific ticker...")
    ticker = "AAPL"  # Replace with a valid ticker from your data
    date = "2024-03-01"  # Replace with a valid date or None
    get_stock_data(ticker, date)