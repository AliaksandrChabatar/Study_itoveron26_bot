# Устанавливаем Python-библиотеку для работы с Телеграмом: pip install pyTelegramBotAPI
# Регистрируем Бота в Telegram через @BotFather, /newbot
# bot's name - Study
# bot's username: Study_itoveron26_bot
# получаем token: 5359361758:AAFLZghBO9bbkcFbiXv9j0Lyn58yUcqBRi4

import telebot
from telebot import types # для создания кнопок

token='5359361758:AAFLZghBO9bbkcFbiXv9j0Lyn58yUcqBRi4'
bot = telebot.TeleBot(token) # обЪявляем бота (создали бота по token-y)

def create_keyboard(): # функция для создания кнопок
    keyboard = types.InlineKeyboardMarkup() # Готовим кнопки
    # По очереди готовим текст и обработчик для каждой кнопки
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать", callback_data='3')
    walk_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn) # добовляем кнопки (в специальный список) на экран
    keyboard.add(eat_btn)
    keyboard.add(sleep_btn)
    keyboard.add(walk_btn)
    keyboard.add(joke_btn)
    return keyboard
# функция срабатывающая при запуске бота
@bot.message_handler(commands=['start']) # чтобы функция сработала, при команде /start
def start_bot(message):
    keyboard=create_keyboard() # создаём кнопки
    bot.send_message(          # пишем сообщение о выборе и
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard  # добавляем все кнопки
    )
# добавляем к кнопкам действия. # Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:       # Если произошло нажати
        if call.data=="1": # и оно соответствует 1, то
            img = open('9-17.jpg','rb') # открывает вставленные картинки
            bot.send_photo(   # сообщение боту на отправку фото
                chat_id=call.message.chat.id, # картинка id сообщения
                photo=img,               # сама картинка
                caption="Картинка воды", # с сообщением
                reply_markup=keyboard)   # и последующими кнопками
            img.close() # закрываем картинку, чтобы не мешала дальнейшей работе
        if call.data == "2":
            img = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('knmxvc.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка большого желания спать",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('lorks9.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка желания гулять",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            img = open('petrosyan.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка типо шутки",
                reply_markup=keyboard)
            img.close()

if __name__=="__main__": # запускаем бота с программой командой /start
    bot.polling(none_stop=True) # Запускаем постоянный опрос бота в Телеграме
    # непрерывно спрашивает у бота, не пришли ли ему какие-то новые сообщения
