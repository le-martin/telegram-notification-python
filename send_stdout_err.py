#!/usr/bin/env python3

import sys

import telegram

lines = [line for line in sys.stdin]
output =  ''.join(lines)
print(output)
telegram.send_message(msg=output)
