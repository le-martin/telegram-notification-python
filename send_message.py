import configparser

import requests


config = configparser.ConfigParser()

message = "TEST"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

print(requests.get(url).json())  # Send message and print request output

