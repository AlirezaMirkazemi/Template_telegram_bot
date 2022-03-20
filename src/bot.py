import os

import telebot
from loguru import logger
from telebot import types

from src.constants import keyboards
from src.utils.io import read_json, write_json

markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = types.KeyboardButton('Connect')
itembtn2 = types.KeyboardButton('Settings')
markup.add(itembtn1, itembtn2)


class Bot:
    """
    telegram bot to randomly connect two strangers to talk.
    """
    def __init__(self):
        logger.info('Bot is ready to use...')
        self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)
        self.commands = self.bot.message_handler(commands=['/start', 'help'])(self.echo_all)

    def run(self):
        logger.info('Bot is starting...')
        self.bot.infinity_polling()

    def echo_all(self, message):
        #write_json(message, './data/messages.json')
        self.bot.send_message(message.chat.id, message.text, reply_markup=keyboards.main)
        


if __name__ == '__main__':
    bot = Bot()
    bot.run()
