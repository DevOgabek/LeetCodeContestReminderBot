# LeetCode Contest Reminder Bot

This Python script is a Telegram bot designed to remind users about the upcoming LeetCode contest. It calculates the time left until the next contest and provides real-time updates.

## Requirements
- Python 3
- `telebot` library
- `decouple` library

## Installation
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
    ```
    pip install telebot python-decouple
    ```
3. Obtain a Telegram Bot API key from the [BotFather](https://core.telegram.org/bots#botfather).
4. Create a `.env` file in the project directory and add your API key:
    ```
    API_KEY=your_telegram_api_key
    ```

## Usage
1. Run the script using Python:
    ```
    python bot.py
    ```
2. Start a conversation with the bot in your Telegram account by searching for its username.
3. Use the `/start` command to begin interacting with the bot.
4. Use the `/timeleft` command to see how much time is left until the next LeetCode contest.

## Features
- Automatically calculates the time left until the next LeetCode contest, which typically starts every Sunday at 7:30 AM.
- Provides real-time updates on the remaining time until the contest starts.
- Responds to user commands to start the interaction and display the time left until the contest.

## How It Works
The bot utilizes the `telebot` library to interact with the Telegram Bot API. It calculates the next contest start time based on the current date and time, and provides updates accordingly. The bot runs continuously, periodically updating the time left until the contest starts.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.