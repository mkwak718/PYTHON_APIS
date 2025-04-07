from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import json
from datetime import datetime
from dateutil import parser
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load stock data from JSON file
def load_stock_data():
    with open('stock_data.json', 'r') as file:
        return json.load(file)

@app.route('/api/stock/<ticker>', methods=['GET'])
def get_stock_data(ticker):
    """Get stock data for a specific ticker. Optionally filter by date."""
    try:
        date = request.args.get('date')
        stock_data = load_stock_data()
        
        # Check if ticker exists
        if ticker not in stock_data:
            return jsonify({'error': f'Ticker {ticker} not found'}), 404
        
        # If date is provided, return data for that specific date
        if date:
            try:
                # Parse and format the date to match our data format
                parsed_date = parser.parse(date).strftime('%Y-%m-%d')
                if parsed_date in stock_data[ticker]:
                    return jsonify({
                        'ticker': ticker,
                        'date': parsed_date,
                        'data': stock_data[ticker][parsed_date]
                    })
                else:
                    return jsonify({'error': f'No data available for {ticker} on {parsed_date}'}), 404
            except ValueError:
                return jsonify({'error': 'Invalid date format'}), 400
        
        # If no date provided, return all data for the ticker
        return jsonify({
            'ticker': ticker,
            'data': stock_data[ticker]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stocks', methods=['GET'])
def list_stocks():
    """Get list of all available stock tickers."""
    try:
        stock_data = load_stock_data()
        return jsonify({
            'tickers': list(stock_data.keys())
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
	app.run(debug=True)
