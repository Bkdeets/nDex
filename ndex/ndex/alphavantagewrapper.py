import os
import requests
import json

KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

def get_current_price(ticker):
	endpoint = '?function=GLOBAL_QUOTE'
	url = BASE_URL + endpoint
	response = requests.get(
		url,
		params = {
			'symbol': ticker,
			'apikey': KEY
		}
	)
	return response.json()
	