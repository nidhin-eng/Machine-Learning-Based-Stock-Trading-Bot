from alpaca_trade_api.rest import REST

API_KEY="PKDO4XWXWWZBH7YOVP9L"
API_SECRET="DOZF5ZJuJS0dwV8eSiNor1cZOpUs4C9ZMJjn3x6X" 
BASE_URL="https://paper-api.alpaca.markets"

api = REST(API_KEY, API_SECRET, BASE_URL)
account = api.get_account()
print(account.status)
