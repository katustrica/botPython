import logging
from config import *

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot, chat, message)
from telegram.ext import (Updater,  CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, InlineQueryHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

status = 0




def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Привет, ты уже получил пароль на почту?' ,
         reply_markup=ReplyKeyboardMarkup([['Да'], ['Нет']], one_time_keyboard=True, resize_keyboard=1))
    context.bot.send_message(chat_id=84203003, text ='Пришел '+ str(update.message.first_name))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def text(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    global status
    if status == 0:
        if update.message.text == 'Да':
            status = 1
            update.message.reply_text("Отправтье свой сайт/инстаграм...",
            reply_markup = ReplyKeyboardMarkup([['Отправил'], ['Есть вопрос']], one_time_keyboard=True,
                                               resize_keyboard=1))
        if update.message.text == "Нет":
            update.message.reply_text( "Перейдите на такой-то сайт, чтобы получить пароль.")
    if status == 1:
        if update.message.text == 'Отправил':
            update.message.reply_text("Мы начали делать скоро пришлем Вам результат.",
                                                                   reply_markup=ReplyKeyboardMarkup([['Супер'], ['Есть доработки']],
                                                                   one_time_keyboard=True,
                                                                   resize_keyboard=1))
            status = 2
        if update.message.text == 'Есть вопрос':
            update.message.reply_text("Отправьте свой вопрос",
            reply_markup = ReplyKeyboardMarkup([['Отправил']], one_time_keyboard=True,
                                               resize_keyboard=1))
            status = -1
    if status == 2:
        if update.message.text == 'Супер':
            status = 3
            update.message.reply_text("Мы начали делать контент план. Ожидайте.",
                                      reply_markup=ReplyKeyboardMarkup([['Отлично'], ['Есть доработки']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
        if update.message.text == 'Есть доработки':
            status = -1
            update.message.reply_text("Отправьте свои доработки",
                                      reply_markup=ReplyKeyboardMarkup([['Отправил доработки']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
    if status == 3:
        if update.message.text == 'Отлично':
            status = 4
            update.message.reply_text("Вот ваш контент на 7 дней и 42 истории. Ждем оценки.",
                                      reply_markup=ReplyKeyboardMarkup([['Супер'], ['Есть уточнения.']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
        if update.message.text == 'Есть доработки.':
            status = -1
            update.message.reply_text("Отправьте свои доработки",
                                      reply_markup=ReplyKeyboardMarkup([['Отправил доработки']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
    if status == 4:
        if update.message.text == 'Супер':
            status = 5
            update.message.reply_text("​Наша работа началась! Первый пост выйдет ... ​числа. Следующий контент план мы вышлем ... ​числа!",
                                      reply_markup=ReplyKeyboardMarkup([['Задать вопрос']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
    if status == 5:
        if update.message.text == 'Задать вопрос':
            status = -1
            update.message.reply_text(
                "Отправтье Ваш вопрос и нажмите кнопку отправил",
                reply_markup=ReplyKeyboardMarkup([['Отправил вопрос']],
                                                 one_time_keyboard=True,
                                                 resize_keyboard=1))

    if status == -1:
        if update.message.text == 'Отправил':
            update.message.reply_text("мы скоро Вам ответим", reply_markup=ReplyKeyboardMarkup([['Отправил'], ['Есть вопрос']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            status = 1

        if update.message.text == 'Отправил доработки':
            update.message.reply_text("мы скоро Вам ответим", reply_markup=ReplyKeyboardMarkup([['Супер'], ['Есть доработки']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            status = 2
        if update.message.text == 'Отправил доработки.':
            update.message.reply_text("мы скоро Вам ответим", reply_markup=ReplyKeyboardMarkup([['Супер'], ['Есть доработки.']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            status = 3
        if update.message.text == 'Отправил уточнения':
            update.message.reply_text("мы скоро Вам ответим", reply_markup=ReplyKeyboardMarkup([['Супер'], ['Есть уточнения.']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            status = 4
        if update.message.text == 'Отправил вопрос':
            status = 5
            update.message.reply_text("мы скоро Вам ответим",
                                      reply_markup=ReplyKeyboardMarkup([['Задать вопрос']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)




def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, text))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()