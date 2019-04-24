import logging
import os
import json
from config import *

from telegram import (ReplyKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

status = 0
messagev = ''
dictionary = {}
name = {}
with open('dictionary.json', 'r') as fp:
    dictionary = json.load(fp)
with open('name.json', 'r') as fp:
    name = json.load(fp)

user = 1


def start(update, context):
    """Send a message when the command /start is issued."""
    global dictionary
    if dictionary.get(str(update.message.from_user.id)) == 666:
        update.message.reply_text(text='admin',
                                  reply_markup=ReplyKeyboardMarkup(
                                      [['Отправить сообщение пользователю'], ['Список клиентов'], ['Следующий этап']],
                                      resize_keyboard=1))
    if dictionary.get(str(update.message.from_user.id)) == None:
        update.message.reply_text('Введите пароль')
        dictionary.update({str(update.message.from_user.id): 0})
        with open('dictionary1.json', 'w') as f:
            f.write(json.dumps(dictionary))
        os.rename('dictionary1.json', 'dictionary.json')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def text(update, context):
    """Echo the user message."""

    # update.message.reply_text(update.message.text)
    global dictionary
    global status
    global name
    global user
    global messagev

    if dictionary.get(str(update.message.from_user.id)) == 0:
        if update.message.text == 'parol123':
            update.message.reply_text('Придумайте себе название')
            dictionary.update({str(update.message.from_user.id): 2})
            with open('dictionary1.json', 'w') as f:
                f.write(json.dumps(dictionary))
            os.rename('dictionary1.json', 'dictionary.json')

        else:
            update.message.reply_text('Неверный пароль, повторите еще.')
    if dictionary.get(str(update.message.from_user.id)) == 2:

        if update.message.text != 'parol123':
            name.update({str(update.message.from_user.id): update.message.text})
            with open('name1.json', 'w') as f:
                f.write(json.dumps(name, ensure_ascii=False))
            os.rename('name1.json', 'name.json')
            dictionary.update({str(update.message.from_user.id): 3})
            with open('dictionary1.json', 'w') as f:
                f.write(json.dumps(dictionary))
            os.rename('dictionary1.json', 'dictionary.json')

            context.bot.send_message(chat_id=84203003,
                                     text='Новый клиент ' + str(name.get(str(update.message.from_user.id))))
            context.bot.send_message(chat_id=295751797,
                                     text='Новый клиент ' + str(name.get(update.message.from_user.id)))
            context.bot.send_message(chat_id=461968123,
                                     text='Новый клиент ' + str(name.get(update.message.from_user.id)))
            update.message.reply_text('Приветствую, ' + str(name.get(str(update.message.from_user.id))) +
                                      '''! Чтобы начать работать над твоим аккаунтом, мне нужно изучить твой бизнес, твою аудиторию и конкурентов.
                                      Для этого тебе надо скинуть информацию о своей компании, а также сайт и социальные сети. Чем подробнее будут данные, тем будет лучше
                                      Как только напишешь всю информацию, нажми кнопку «Отправить».
                                      Если у тебя есть вопросы, нажми на кнопку «Задать вопрос».
                                      ''',
                                      reply_markup=ReplyKeyboardMarkup([['Отправить'], ['Задать вопрос']],

                                                                       resize_keyboard=1))
    if dictionary.get(str(update.message.from_user.id)) == 3:
        messagev += update.message.text + '\n'
        messagev.replace(str(name.get(str(update.message.from_user.id))), '')
        if update.message.text == 'Отправить':
            messagev = messagev.replace('Отправить', '')
            update.message.reply_text(str(name.get(str(update.message.from_user.id))) + ''', этот этап очень важный!
Напиши, что бы ты хотел видеть в своём аккаунте? Какие профили в Инстаграм тебе нравятся по дизайну, подаче, стилю?
А также, напиши, что бы ты никогда не хотел видеть в своём Инстаграм?
Чем больше будет информации, тем лучше.
После того, как напишешь всю информацию, жми «Отправить».
Если нечего скидывать, так и отвечай «Нет особых пожеланий».
''',
                                      reply_markup=ReplyKeyboardMarkup([['Отправить.'], ['Нет особых пожеланий']],

                                                                       resize_keyboard=1))
            context.bot.send_message(chat_id=84203003,
                                     text='____ИНФА О КОМПАНИИ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ИНФА О КОМПАНИИ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ИНФА О КОМПАНИИ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            messagev = ''
            dictionary.update({str(update.message.from_user.id): 4})

            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

        if update.message.text == 'Задать вопрос':
            messagev = messagev.replace('Задать вопрос', '')
            update.message.reply_text("мы скоро Вам ответим")
            context.bot.send_message(chat_id=84203003, text='____ВОПРОС____\n - от ' + str(
                name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797, text='____ВОПРОС____\n - от ' + str(
                name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123, text='____ВОПРОС____\n - от ' + str(
                name.get(update.message.from_user.id)) + '\n\n' + messagev)

            messagev = ''
    if dictionary.get(str(update.message.from_user.id)) == 4:
        messagev += update.message.text + '\n'
        if update.message.text == 'Отправить.':
            messagev = messagev.replace('Отправить.', '')
            messagev = messagev.replace('Отправить', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
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
            ''', reply_markup=ReplyKeyboardMarkup([['Отправить логин и пароль', 'Задать вопрос']],

                                                  resize_keyboard=1))
            dictionary.update({str(update.message.from_user.id): 8})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

        if update.message.text == 'Нет особых пожеланий':
            dictionary.update({str(update.message.from_user.id): 8})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

            context.bot.send_message(chat_id=84203003, 
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + 'нет особых пожеланий')
            context.bot.send_message(chat_id=295751797,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + 'нет особых пожеланий')
            context.bot.send_message(chat_id=461968123,
                                     text='____КАКИЕ ДОЛЖНЫ БЫТЬ ПОСТЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + 'нет особых пожеланий')

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
''', reply_markup=ReplyKeyboardMarkup([['Отправить логин и пароль', 'Задать вопрос']],
                                      resize_keyboard=1))
        if update.message.text == 'Задать вопрос':
            dictionary.update({str(update.message.from_user.id): 4})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

            context.bot.send_message(chat_id=84203003,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            messagev = ''
    if dictionary.get(str(update.message.from_user.id)) == 5:
        if update.message.text == 'Мне все нравится':
            dictionary.update({str(update.message.from_user.id): 6})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

            update.message.reply_text(str(name.get(str(update.message.from_user.id))) + ''', супер!
В течении двух недель я буду выкладывать посты в твоём аккаунте.
Если у тебя появятся вопросы по любой теме, смело пиши и жми на кнопку «Задать вопрос».''',
                                      reply_markup=ReplyKeyboardMarkup(
                                          [['Задать вопрос']],
                                          resize_keyboard=1))
        if update.message.text == 'Есть доработки':
            dictionary.update({str(update.message.from_user.id): 7})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

            update.message.reply_text(str(name.get(str(update.message.from_user.id))) + ''', опиши, что тебе не понравилось?
Что бы ты хотел видеть или изменить?
После того, как напишешь всю информацию, жми на кнопку «Отправить дизайн / темы / текст ».''',
                                      reply_markup=ReplyKeyboardMarkup(
                                          [['Изменить дизайн'], ['Изменить темы'], ['Изменить текст']],
                                          resize_keyboard=1))
    if dictionary.get(str(update.message.from_user.id)) == 6:
        messagev += update.message.text + '\n'
        if update.message.text == 'Задать вопрос':
            messagev = messagev.replace('Задать вопрос', '')
            update.message.reply_text("мы скоро Вам ответим")
            messagev = messagev.replace('Мне все нравится', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ВОПРОС О ПУБЛИКАЦИЯХ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ВОПРОС О ПУБЛИКАЦИЯХ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)

            context.bot.send_message(chat_id=295751797,
                                     text='____ВОПРОС О ПУБЛИКАЦИЯХ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            messagev = ''
    if dictionary.get(str(update.message.from_user.id)) == 7:
        messagev += update.message.text + '\n'
        if update.message.text == 'Изменить дизайн':
            messagev = messagev.replace('Изменить дизайн', '')
            messagev = messagev.replace('Отправить', '')
            messagev = messagev.replace('Есть доработки', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ДИЗАЙН____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ДИЗАЙН____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ДИЗАЙН____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            update.message.reply_text(text='Мы исправим и вышлим новую версию')
            messagev = ''
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

        if update.message.text == 'Изменить темы':
            messagev = messagev.replace('Изменить темы', '')
            messagev = messagev.replace('Отправить', '')
            messagev = messagev.replace('Есть доработки', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ТЕМЫ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ТЕМЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ТЕМЫ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            update.message.reply_text(text='Мы исправим и вышлим новую версию')
            messagev = ''
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

        if update.message.text == 'Изменить текст':
            messagev = messagev.replace('Изменить текст', '')
            messagev = messagev.replace('Отправить', '')
            messagev = messagev.replace('Есть доработки', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ТЕКСТ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ТЕКСТ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ТЕКСТ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            update.message.reply_text(text='Мы исправим и вышлим новую версию')
            messagev = ''
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

    if dictionary.get(str(update.message.from_user.id)) == 8:
        messagev += update.message.text + '\n'
        messagev.replace('Нет особых пожеланий', '')
        messagev.replace('Задать вопрос', '')
        if update.message.text == 'Отправить логин и пароль':
            dictionary.update({str(update.message.from_user.id): 4})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            messagev = messagev.replace('Отправить логин и пароль', '')
            
            context.bot.send_message(chat_id=84203003,
                                     text='____ЛОГИН И ПАРОЛЬ____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ЛОГИН И ПАРОЛЬ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ЛОГИН И ПАРОЛЬ____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            messagev = ''
        if update.message.text == 'Задать вопрос':
            dictionary.update({str(update.message.from_user.id): 4})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            messagev = messagev.replace('Задать вопрос', '')
            context.bot.send_message(chat_id=84203003,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=461968123,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(str(update.message.from_user.id))) + '\n\n' + messagev)
            context.bot.send_message(chat_id=295751797,
                                     text='____ВОПРОС____\n - от ' + str(
                                         name.get(update.message.from_user.id)) + '\n\n' + messagev)
            messagev = ''

    if dictionary.get(str(update.message.from_user.id)) == 666:
        messagev = ''
        if update.message.text == 'Отправить сообщение пользователю':
            dictionary.update({str(update.message.from_user.id): 667})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            update.message.reply_text('Введи ID пользователя, кому хочешь написать.')

        if update.message.text == 'Следующий этап':
            dictionary.update({str(update.message.from_user.id): 669})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            update.message.reply_text('Введи ID пользователя, который перейдет на следующий этап.')

        if update.message.text == 'Список клиентов':
            for i in dictionary.items():
                context.bot.send_message(chat_id=84203003,
                                         text='ID- ' + str(i[0]) + "\nSTATUS- " + str(i[1]) + '\nNAME- ' + name.get((i[0])))
                context.bot.send_message(chat_id=295751797,
                                         text='ID- ' + str(i[0]) + "\nSTATUS- " + str(i[1]) + '\nNAME- ' + name.get((i[0])))
                context.bot.send_message(chat_id=461968123,
                                         text='ID- ' + str(i[0]) + "\nSTATUS- " + str(i[1]) + '\nNAME- ' + name.get(
                                             (i[0])))
                
            messagev = ''

    if dictionary.get(str(update.message.from_user.id)) == 667:
        if update.message.text != 'Отправить сообщение пользователю':
            user = int(update.message.text)
            update.message.reply_text(text='Что хочешь отправить пользователю - ' + str(
                name.get(user)) + '\n и отправь S ' + '\n Если хочешь вернуться назад, то отправь B')
            dictionary.update({str(update.message.from_user.id): 668})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

    if dictionary.get(str(update.message.from_user.id)) == 668:
        if update.message.text == 'B':
            dictionary.update({str(update.message.from_user.id): 666})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

            update.message.reply_text(text='Ты вернулся в главное меню',
                                      reply_markup=ReplyKeyboardMarkup(
                                          [['Отправить сообщение пользователю'], ['Список клиентов'],
                                           ['Следующий этап']],
                                          resize_keyboard=1))
        if update.message.text == 'S':
            context.bot.send_message(chat_id=user, text=messagev)
            dictionary.update({str(update.message.from_user.id): 666})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            update.message.reply_text(
                text='Ты вернулся в главное меню, а сообщение \n\n _______\n' + messagev + '\n ОТПРАВЛЕНО',
                reply_markup=ReplyKeyboardMarkup(
                    [['Отправить сообщение пользователю'], ['Список клиентов'], ['Следующий этап']],
                    resize_keyboard=1))
            messagev = ''
        else:
            messagev += update.message.text + '\n'
            messagev = messagev.replace(str(user), '')
            messagev = messagev.replace(str(name.get(user)), '')

    if dictionary.get(str(update.message.from_user.id)) == 669:
        if update.message.text != 'Следующий этап':
            user = int(update.message.text)
            update.message.reply_text(text='Пользователь - ' + str(
                name.get(str(user))) + '\n уверен?',
                                      reply_markup=ReplyKeyboardMarkup(
                                          [['Да'], ['Нет']],
                                          resize_keyboard=1))
            dictionary.update({str(update.message.from_user.id): 670})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))

    if dictionary.get(str(update.message.from_user.id)) == 670:
        if update.message.text == 'Да':
            dictionary.update({str(update.message.from_user.id): 666})
            dictionary.update({str(user): 5})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            update.message.reply_text(text='Ты вернулся в главное меню, cтатус пользователя' + str(
                name.get(str(user))) + ' изменен на -' + str(dictionary.get(str(user))),
                                      reply_markup=ReplyKeyboardMarkup(
                                          [['Отправить сообщение пользователю'], ['Список клиентов'],
                                           ['Следующий этап']],
                                          resize_keyboard=1))
            context.bot.send_message(chat_id=user,
                                     text='Напиши "Мне все нравится", если у ты доволен. Либо "Есть доработки", если они имеются)')
        if update.message.text == 'Нет':
            dictionary.update({str(update.message.from_user.id): 666})
            with open('dictionary.json', 'w') as f:
                f.write(json.dumps(dictionary))
            update.message.reply_text(
                text='Ты вернулся в главное меню',
                reply_markup=ReplyKeyboardMarkup(
                    [['Отправить сообщение пользователю'], ['Список клиентов'], ['Следующий этап']],
                    resize_keyboard=1))
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
