# Telegram Python Notification Bot
This is a simple Telegram bot that sends notifications to a specified chat ID using the Telegram Bot API. The bot is built using Python and the `requests` library to send HTTP requests to the Telegram API. This project was inspired by this [tutorial](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e).

## Requirements
### Python
- Python 3.x
- `requests` library
- `python-dotenv` library (for loading the `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` as environment variables)
### Telegram
- A Telegram account
- Create Telegram bot user:
    1. Create a new bot by sending `/start` to the [BotFather](https://t.me/botfather) on Telegram.
    2. Send the command `/newbot` to create a new bot.
    3. Save the token in a secure place, as you will need it to send messages.
- Getting your Telegram chat ID:
    1. Send the `\start` message to your bot.
    2. Use the following URL to get your chat ID:
        ```
        https://api.telegram.org/bot<your_bot_token>/getUpdates
        ```
    3. Look for the `message/from` object in the response, and find the `id` field. This is your chat ID.

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:le-martin/telegram-notification-python.git
    cd telegram-notification-python
    ```
2. To install the required libraries, we recommend using a virtual environment. First, we introduce how to do this with [uv](https://docs.astral.sh/uv/) (recommended) and then alternatively with `venv` (standard library). We do not recommend using `pip` directly in the global environment.
    - Using `uv`:
        ```bash
        uv sync
        ```
    - Using `venv`:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
        pip install -r requirements.txt
        ```
3. Create a `.env` file in the root directory of the project and add your Telegram bot token and chat ID in that file. To do this, you can use the template provided:
    ```bash
    cp .env_template .env
    ```

    **Alternatively:** You can also create the `.env` file manually by creating a new file named `.env` in the root directory of the project and adding the following lines:
    ```bash
    # .env
    # Telegram Bot Token
    CHAT_ID=<ADD-CHAT-ID-HERE>
    # Telegram Chat ID
    TOKEN=<ADD-TOKEN-HERE>
    ```
4. Then, open the `.env` file and add your bot token and chat ID:
    - Replace `<ADD-CHAT-ID-HERE>` with the chat ID of the user or group you want to send notifications to. You can find your chat ID by sending a message to your bot and checking the updates using the following URL:
    ```
    https://api.telegram.org/bot<your_bot_token>/getUpdates
    ```
    - Replace `<ADD-TOKEN-HERE>` with the token you received from the BotFather when you created your bot.
5. Save the `.env` file.

## Usage
To send a notification, run the following command:
```bash
python telegram.py "Your notification message"
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
