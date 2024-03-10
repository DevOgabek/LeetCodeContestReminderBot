import telebot
import datetime
import threading
import time
import pytz
from decouple import config

API_KEY = config("API_KEY")

bot = telebot.TeleBot(API_KEY)

# Define GMT+5 Time Zone
leetcode_timezone = pytz.timezone("Asia/Karachi")

def next_contest_start():
    today = datetime.datetime.now(leetcode_timezone)
    next_sunday_date = today + datetime.timedelta(days=(6 - today.weekday()) % 7)
    contest_start_time = next_sunday_date.replace(
        hour=7, minute=30, second=0, microsecond=0
    )
    if datetime.datetime.now(leetcode_timezone) >= contest_start_time:
        next_sunday_date += datetime.timedelta(weeks=1)
        contest_start_time = next_sunday_date.replace(
            hour=7, minute=30, second=0, microsecond=0
        )
    return contest_start_time


def is_contest_started():
    now = datetime.datetime.now(leetcode_timezone)
    start_time = next_contest_start()
    if start_time <= now <= start_time + datetime.timedelta(hours=1):
        return True
    return False


def get_time_left():
    if is_contest_started():
        return "The LeetCode contest has already started!"
    contest_start_time = next_contest_start()
    time_difference = contest_start_time - datetime.datetime.now(leetcode_timezone)
    if time_difference.total_seconds() > 0:
        days, seconds = time_difference.days, time_difference.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"Starts in {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    else:
        return "The LeetCode contest has already started!"


def update_time():
    while True:
        new_message_ids = {}
        time_left = get_time_left()
        for chat_id, current_message_id in message_ids.items():
            try:
                message = bot.edit_message_text(
                    chat_id=chat_id, message_id=current_message_id, text=time_left
                )
                if message.text != time_left:
                    new_message_ids[chat_id] = message.message_id
            except Exception as e:
                print(f"Error updating message: {e}")
        message_ids.update(new_message_ids)
        time.sleep(1)



message_ids = {}

update_thread = threading.Thread(target=update_time)
update_thread.daemon = True
update_thread.start()


@bot.message_handler(commands=["start"])
def send_welcome(message):
    reply = "Welcome! Use /timeleft to see how much time is left until the next LeetCode contest."
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=["timeleft"])
def time_left(message):
    response = get_time_left()
    if message.chat.id in message_ids:
        del message_ids[message.chat.id]
    sent_message = bot.send_message(message.chat.id, response)
    message_ids[message.chat.id] = sent_message.id


bot.polling()
