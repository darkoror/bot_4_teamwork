from telebot import types


def image_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    callback_button_0 = types.InlineKeyboardButton(text='ukr', callback_data='ukr.image')
    callback_button_1 = types.InlineKeyboardButton(text='ru', callback_data='ru.image')
    callback_button_2 = types.InlineKeyboardButton(text='en', callback_data='en.image')

    keyboard.add(callback_button_0, callback_button_1, callback_button_2)

    return keyboard


def voice_keyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    callback_button_0 = types.InlineKeyboardButton(text='ukr', callback_data='ukr.voice')
    callback_button_1 = types.InlineKeyboardButton(text='ru', callback_data='ru.voice')
    callback_button_2 = types.InlineKeyboardButton(text='en', callback_data='en.voice')
    keyboard.add(callback_button_0, callback_button_1, callback_button_2)

    return keyboard
