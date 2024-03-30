#!/usr/bin/env python3

import configparser
import math
import socket
import sys
import time

import requests


def send_message(msg: str) -> None:
    config = configparser.ConfigParser()
    config.read('config.ini')
    TOKEN: str = config['DEFAULT']['TOKEN']
    CHAT_ID: str = config['DEFAULT']['CHAT_ID']
    HOSTNAME: str= socket.gethostname()
    now: str = time.strftime("%I:%M%p on %B %d, %Y")
    new_msg: str = f"{HOSTNAME}({now}):\n{msg}"
    num_msg: int = math.ceil(len(new_msg) / 4096)
    for i in range(num_msg):
        if i != num_msg - 1:
            split_msg = new_msg[4096 * i:4096 * (i + 1)]
        else:
            split_msg = new_msg[4096 * i:]
        url: str = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={split_msg}"
        print(requests.get(url).json())  # Send message and print request output


if __name__ == '__main__':
    message: str = ': '.join(sys.argv[1:])
    send_message(msg=message)
