import requests

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print(requests.get(url).json())
