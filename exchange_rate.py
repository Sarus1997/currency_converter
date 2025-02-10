import requests

API_KEY = "  "  # ใช้ API key ของคุณ
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(base_currency, target_currency):
    try:
        url = BASE_URL + base_currency
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if target_currency in data["conversion_rates"]:
            return data["conversion_rates"][target_currency]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("⚠️ API Error:", e)
        return None
