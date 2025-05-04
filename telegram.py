#!/usr/bin/env python3
# telegram.py
# -*- coding: utf-8 -*-
"""
Send a message to a Telegram chat using the Bot API.

Usage:
    python telegram.py "Your message here"
"""

import os
import socket
import logging
import argparse
from datetime import datetime
from textwrap import wrap

import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter, Retry

# ─── Configuration ──────────────────────────────────────────────────────────────

load_dotenv()  # reads .env
TOKEN   = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
if not TOKEN or not CHAT_ID:
    raise SystemExit("Error: TOKEN and CHAT_ID must be set in your .env file.")

API_URL    = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
MAX_LENGTH = 4096  # Telegram max message size

# ─── Logging & HTTP Session ────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

session = requests.Session()
retries = Retry(total=3, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))


# ─── Core Functionality ────────────────────────────────────────────────────────

def send_message(text: str) -> None:
    """Send one or more (auto-split) messages to Telegram."""
    hostname  = socket.gethostname()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header    = f"{hostname} @ {timestamp}"
    full_text = f"{header}\n{text}"

    chunks = wrap(full_text, MAX_LENGTH,
                  break_long_words=True,
                  replace_whitespace=False)

    for idx, chunk in enumerate(chunks, start=1):
        payload = {'chat_id': CHAT_ID, 'text': chunk}

        logging.info(f"Sending chunk {idx}/{len(chunks)} ({len(chunk)} chars)")
        resp = session.post(API_URL, data=payload, timeout=5)
        try:
            resp.raise_for_status()
        except requests.HTTPError as exc:
            logging.error(f"Telegram API error: {exc} – response was {resp.text!r}")
        else:
            ok = resp.json().get('ok', False)
            if not ok:
                logging.warning(f"Telegram returned not-ok: {resp.json()}")
            else:
                logging.info("Chunk sent successfully.")


# ─── CLI Entry Point ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Send a message via Telegram Bot API"
    )
    parser.add_argument(
        'message', nargs='+',
        help="Message text to send (you can split over multiple words)"
    )
    args = parser.parse_args()

    text = ' '.join(args.message)

    send_message(text)


if __name__ == '__main__':
    main()
