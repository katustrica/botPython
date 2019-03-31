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
NUser = 'Name'
messagev = ''
dictionary = {84203003 : 666}
name = {84203003 : 'admin'}


def start(update, context):
    """Send a message when the command /start is issued."""
    global  dictionary
    update.message.reply_text(str(update.message.from_user.id) + '\n' + str(dictionary.get(update.message.from_user.id)) + str(name.get(update.message.from_user.id)))
    if dictionary.get(update.message.from_user.id) == 666:
        update.message.reply_text(text= 'admin',
            reply_markup=ReplyKeyboardMarkup([['Отправить сообщение пользователю'], ['Список клиентов'],['Запомни chatID']],
                                             one_time_keyboard=True,
                                             resize_keyboard=1))
    if dictionary.get(update.message.from_user.id) == None:
        update.message.reply_text('Введите пароль')
        dictionary.update({update.message.from_user.id: 0})


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def text(update, context):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    global  dictionary
    global status
    global name
    global messagev
    if dictionary.get(update.message.from_user.id) == 0:
        if update.message.text == 'parol123':
            update.message.reply_text('Придумайте себе название')
            dictionary.update({update.message.from_user.id: 2})
        else:
            update.message.reply_text('Неверный пароль, повторите еще.')
    if dictionary.get(update.message.from_user.id) == 2:

        if update.message.text != 'parol123':
            name.update({update.message.from_user.id :update.message.text})
            dictionary.update({update.message.from_user.id: 3})
            context.bot.send_message(chat_id=84203003, text='Новый клиент ' + NUser)
            update.message.reply_text('Приветствую, ' + NUser +
'''! Чтобы начать работать над твоим аккаунтом, мне нужно изучить твой бизнес, твою аудиторию и конкурентов.
⠀
Для этого тебе надо скинуть информацию о своей компании, а также сайт и социальные сети. Чем подробнее будут данные, тем будет лучше👍
⠀
Как только напишешь всю информацию, нажми кнопку «Отправить».
Если у тебя есть вопросы, нажми на кнопку «Задать вопрос».
''',
                                          reply_markup=ReplyKeyboardMarkup([['Отправить'], ['Задать вопрос']],
                                                                           one_time_keyboard=True,
                                                                           resize_keyboard=1))
    if dictionary.get(update.message.from_user.id) == 3:
        messagev += update.message.text + '\n'
        if update.message.text == 'Отправить':
            messagev = messagev.replace('Отправить', '')
            update.message.reply_text(NUser+''', этот этап очень важный😌
Напиши, что бы ты хотел видеть в своём аккаунте? Какие профили в Инстаграм тебе нравятся по дизайну, подаче, стилю?
А также, напиши, что бы ты никогда не хотел видеть в своём Инстаграм?
Чем больше будет информации, тем лучше👍
После того, как напишешь всю информацию, жми «Отправить».
Если нечего скидывать, так и отвечай «Нет особых пожеланий».
''',
                                                                   reply_markup=ReplyKeyboardMarkup([['Отправить.'], ['Нет особых пожеланий']],
                                                                   one_time_keyboard=True,
                                                                   resize_keyboard=1))
            context.bot.send_message(chat_id=84203003, text='____ИНФА О КОМПАНИИ____\n - от '+NUser+'\n\n'+messagev)
            messagev = ''
            dictionary.update({update.message.from_user.id: 4})
        if update.message.text == 'Задать вопрос':
            messagev = messagev.replace('Задать вопрос', '')
            update.message.reply_text("мы скоро Вам ответим")
            context.bot.send_message(chat_id=84203003, text='____ВОПРОС____\n - от '+NUser+'\n\n'+messagev)
            messagev = ''
    if dictionary.get(update.message.from_user.id) == 4:
        messagev += update.message.text + '\n'
        if update.message.text == 'Отправить.':
            messagev = messagev.replace('Отправить.', '')
            messagev = messagev.replace('Отправить', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + NUser + '\n\n' + messagev)
            messagev = ''
            update.message.reply_text('''Я уже начал обрабатывать твою информацию.⠀
            Отправь свой логин и пароль от Инстаграма, чтобы мы могли подключить:
            - масслайкинг и массфоловинг
            - приветсвенное сообщение
            - автоматическое выкладывание постов
            И сделать базовое оформление твоей страницы.
            ⠀
            Через 4-7 дней мы скинем всю информацию и посты на 2 недели.
             ⠀
            Как только напишешь всю информацию, нажми кнопку «Отправить».
            Если у тебя есть вопросы, нажми кнопку «Задать вопрос».
            ''', reply_markup=ReplyKeyboardMarkup([['Отправить', 'Задать вопрос']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            dictionary.update({update.message.from_user.id: 5})
        if update.message.text == 'Нет особых пожеланий':
            dictionary.update({update.message.from_user.id: 5})
            messagev = ''
            update.message.reply_text('''Я уже начал обрабатывать твою информацию.⠀
Отправь свой логин и пароль от Инстаграма, чтобы мы могли подключить:
- масслайкинг и массфоловинг
- приветсвенное сообщение
- автоматическое выкладывание постов
И сделать базовое оформление твоей страницы.
⠀
Через 4-7 дней мы скинем всю информацию и посты на 2 недели.
 ⠀
Как только напишешь всю информацию, нажми кнопку «Отправить».
Если у тебя есть вопросы, нажми кнопку «Задать вопрос».
''', reply_markup=ReplyKeyboardMarkup([['Отправить', 'Задать вопрос']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
    if dictionary.get(update.message.from_user.id) == 5:
        if update.message.text == 'Мне все нравится, можно публиковать':
            dictionary.update({update.message.from_user.id: 6})
            update.message.reply_text(NUser+''', супер 👍
В течении двух недель я буду выкладывать посты в твоём аккаунте.
Если у тебя появятся вопросы по любой теме, смело пиши и жми на кнопку «Задать вопрос».''',
                                      eply_markup=ReplyKeyboardMarkup([['Изменить дизайн'], ['Изменить темы'], ['Изменить текст']],one_time_keyboard=True,resize_keyboard=1))
        if update.message.text == 'Есть доработки.':
            dictionary.update({update.message.from_user.id: 7})
            update.message.reply_text(NUser + ''', опиши, что тебе не понравилось?
Что бы ты хотел видеть или изменить?
После того, как напишешь всю информацию, жми на кнопку «Отправить дизайн / темы / текст ».''',
                                      reply_markup=ReplyKeyboardMarkup([['Изменить дизайн'], ['Изменить темы'], ['Изменить текст']],one_time_keyboard=True,resize_keyboard=1))
    if dictionary.get(update.message.from_user.id) == 6:
        messagev += update.message.text + '\n'
        if update.message.text == 'Задать вопрос.':
            dictionary.update({update.message.from_user.id: 7})
            messagev = messagev.replace('Задать вопрос', '')
            update.message.reply_text("мы скоро Вам ответим")
            context.bot.send_message(chat_id=84203003, text='____ВОПРОС О ПУБЛИКАЦИЯХ____\n - от ' + NUser + '\n\n' + messagev)
            messagev = ''
    if dictionary.get(update.message.from_user.id) == 7:
        messagev += update.message.text + '\n'
        if update.message.text == 'Изменить дизайн':
            messagev = messagev.replace('Изменить дизайн', '')
            messagev = messagev.replace('Отправить', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ДИЗАЙН____\n - от ' + NUser + '\n\n' + messagev)
            update.message.reply_text(reply_markup=ReplyKeyboardMarkup([['Мне все нравится, можно публиковать', 'Есть доработки.']],
                                                                       one_time_keyboard=True,
                                                                       resize_keyboard=1))
            messagev = ''
        if update.message.text == 'Изменить темы':
            messagev = messagev.replace('Изменить темы', '')
            messagev = messagev.replace('Отправить', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ТЕМЫ____\n - от ' + NUser + '\n\n' + messagev)
            update.message.reply_text(
                reply_markup=ReplyKeyboardMarkup([['Мне все нравится, можно публиковать', 'Есть доработки.']],
                                                 one_time_keyboard=True,
                                                 resize_keyboard=1))
            messagev = ''
        if update.message.text == 'Изменить текст':
            messagev = messagev.replace('Изменить текст', '')
            messagev = messagev.replace('Отправить', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ТЕКСТ____\n - от ' + NUser + '\n\n' + messagev)
            update.message.reply_text(
                reply_markup=ReplyKeyboardMarkup([['Мне все нравится, можно публиковать', 'Есть доработки.']],
                                                 one_time_keyboard=True,
                                                 resize_keyboard=1))
            messagev = ''
    if dictionary.get(update.message.from_user.id) == 666:
        messagev += ' '+ update.message.text
        if update.message.text == 'Отправить сообщение пользователю':
            messagev = messagev.replace('Отправить сообщение пользователю', '')
            word = str(messagev.split(' ')[0])
            messagev = messagev.replace(word, '')
            context.bot.send_message(chat_id=int(word),
                                     text = messagev)
        if update.message.text == 'Список клиентов':
            for i in dictionary.items():
                context.bot.send_message(chat_id=84203003,
                                     text='ID- '+str(i[0])+"\nSTATUS- "+str(i[1]))
            messagev = ''
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
