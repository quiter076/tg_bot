from forbot import *
import telebot
from telebot import types
token = '8495971064:AAHFlqhm3ZZVcqCnOQLjMxXVK-N4B-4PtX0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Начать')
    markup.add(button1)
    bot.send_message(message.chat.id, '💜Добро пожаловать в бот расписания кружков УУНиТ💜', reply_markup=markup)

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Начать')
    markup.add(button1)

user_states = {}
@bot.message_handler(content_types='text')
def message_reply(message):
    user_id = message.from_user.id
    current_section = user_states.get(user_id, '')

    sections_responses = {
        'Танцы': [dance_ensemble_yeshlek, dance_ensemble_allegro, dance_ensemble_irandek],
        'Пение': [song_septima, song_moment_more, song_aktamir],
        'Театр': [teatr_oskon, teatr_grotesk, teatr_selet],
        'Спорт': [sport_green, sport_voshod, sport_ikar],
        'По интересам': [anime, math_club]
    }


    if message.text == 'Начать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Танцы')
        button2 = types.KeyboardButton('Пение')
        button3 = types.KeyboardButton('Театр')
        button4 = types.KeyboardButton('Спорт')
        button5 = types.KeyboardButton('По интересам')
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, 'Выберите направление кружка:', reply_markup=markup)
        #обнуляем значение
        user_states[user_id] = ''

    elif message.text in sections_responses:
        if message.text == 'Танцы':
             current_section = 'Танцы'
             user_states[user_id] = 'Танцы'
        if message.text == 'Пение':
             current_section = 'Пение'
             user_states[user_id] = 'Пение'
        if message.text == 'Театр':
             current_section = 'Театр'
             user_states[user_id] = 'Театр'
        if message.text == 'Спорт':
             current_section = 'Спорт'
             user_states[user_id] = 'Спорт'
        if message.text == 'По интересам':
             current_section = 'По интересам'
             user_states[user_id] = 'По интересам'

        club_list = sections_responses[message.text]
        answer = ''
        for club_info in club_list:
            answer += f'{club_info}\n'
        bot.send_message(message.chat.id, answer)

        # Добавляем кнопку для возврата
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        button6 = types.KeyboardButton('Выбрать кружок')
        markup.add(back_button, button6)
        bot.send_message(message.chat.id, 'Выберите следующее действие:', reply_markup=markup)

    elif message.text == 'В главное меню':
        user_states[user_id] = ''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Начать')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Возврат в главное меню', reply_markup=markup)

    elif message.text == 'Выбрать кружок':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button7 = types.KeyboardButton('1')
        button8 = types.KeyboardButton('2')
        button9 = types.KeyboardButton('3')
        markup.add(button7, button8, button9)
        bot.send_message(message.chat.id, 'Какой кружок вам интересен?', reply_markup=markup)

    elif message.text in ['1', '2', '3']:
        if current_section in sections_info:
            bot.send_message(message.chat.id, {sections_info[current_section][int(message.text) - 1]})
        else:
            bot.send_message(message.chat.id, 'Кружка с таким номером нет')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = types.KeyboardButton('В главное меню')
        markup.add(back_button)
        bot.send_message(message.chat.id, 'В главное меню?', reply_markup=markup)

    elif message.txt == 'В главное меню':
        user_states[user_id] = ''
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Начать')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Возврат в главное меню', reply_markup=markup)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()