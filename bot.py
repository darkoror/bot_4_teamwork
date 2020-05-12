import telebot
import os

import voice_recognizer
import image_recognizer
import constants
import converter
import keyboards


bot = telebot.TeleBot(constants.test_token)


@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(message.from_user.id, "Welcome!")


@bot.message_handler(content_types=['text'])
def handler_text(message):
    bot.send_message(message.from_user.id, message.text)


@bot.message_handler(content_types=['photo'])
def photo_msg(message):
    bot.reply_to(message, 'Вкажіть мову тексту на картинці', reply_markup=keyboards.image_keyboard())

    """tg_photo_msg = bot.get_file(message.photo[2].file_id)               # downloading file (photo)
    downloaded_photo = bot.download_file(tg_photo_msg.file_path)
    jpg_file = message.json['photo'][2]['file_unique_id'] + '.jpg'
    open(jpg_file, 'wb').write(downloaded_photo)
    text_from_photo = image_recognizer.photo_2_text(jpg_file)
    os.remove(jpg_file)
    bot.send_message(message.from_user.id, text_from_photo)"""


@bot.message_handler(content_types=['voice'])
def voice_msg(message):
    bot.reply_to(message, 'Вкажіть мову голосового повідомлення', reply_markup=keyboards.voice_keyboard())

    """tg_voice_msg = bot.get_file(message.voice.file_id)
    downloaded_voice = bot.download_file(tg_voice_msg.file_path)                # downloading file (voice) from telegram
    oga_file = message.json['voice']['file_unique_id'] + '.oga'
    open(oga_file, 'wb').write(downloaded_voice)                                    # write down voice into file (.ogg)

    wav_file = converter.oga_2_wav(oga_file)                                           # convert .oga to .wav

    text_from_voice = voice_recognizer.voice_2_text(wav_file)   # recognize the speech from .wav using "speech_recognition"

    os.remove(oga_file)
    os.remove(wav_file)
    bot.send_message(message.from_user.id, text_from_voice)                       # send the recognized text to the user"""


@bot.callback_query_handler(func=lambda call: 'image' in call.data)
def image_keyboard(call):
    image_lang = call.data.split('.')[0]

    tg_photo_msg = bot.get_file(call.message.reply_to_message.photo[2].file_id)  # downloading file (photo)
    downloaded_photo = bot.download_file(tg_photo_msg.file_path)
    jpg_file = call.message.json['reply_to_message']['photo'][2]['file_unique_id'] + '.jpg'
    open(jpg_file, 'wb').write(downloaded_photo)

    if image_lang == 'en':
        text_from_photo = image_recognizer.photo_2_text(jpg_file)

    elif image_lang == 'ukr':
        text_from_photo = ''

    elif image_lang == 'ru':
        text_from_photo = ''

    else:
        text_from_photo = 'bot doesnt support this language'

    os.remove(jpg_file)

    bot.reply_to(call.message.reply_to_message, text_from_photo)
    # smth


@bot.callback_query_handler(func=lambda call: 'voice' in call.data)
def voice_keyboard(call):
    voice_lang = call.data.split('.')[0]

    tg_voice_msg = bot.get_file(call.message.reply_to_message.voice.file_id)
    downloaded_voice = bot.download_file(tg_voice_msg.file_path)                # downloading file (voice) from telegram
    oga_file = call.message.json['reply_to_message']['voice']['file_unique_id'] + '.oga'
    open(oga_file, 'wb').write(downloaded_voice)                                # write down voice into file (.oga)

    wav_file = converter.oga_2_wav(oga_file)                                    # convert .oga to .wav

    if voice_lang == 'en':
        text_from_voice = voice_recognizer.voice_2_en(wav_file)

    elif voice_lang == 'ukr':
        text_from_voice = voice_recognizer.voice_2_ukr(wav_file)

    elif voice_lang == 'ru':
        text_from_voice = voice_recognizer.voice_2_ru(wav_file)

    else:
        text_from_voice = 'smth'

    os.remove(oga_file)
    os.remove(wav_file)

    bot.reply_to(call.message.reply_to_message, text_from_voice)


if __name__ == '__main__':
    bot.polling(none_stop=True)
