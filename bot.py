import telebot
import os

import voice_recognizer
import image_recognizer
import constants
import converter


bot = telebot.TeleBot(constants.test_token)


@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(message.from_user.id, "Welcome!")


@bot.message_handler(content_types=['text'])
def handler_text(message):
    bot.send_message(message.from_user.id, message.text)


@bot.message_handler(content_types=['photo'])
def handler_photo(message):
    tg_photo_msg = bot.get_file(message.photo[2].file_id)               # downloading file (voice)
    downloaded_photo = bot.download_file(tg_photo_msg.file_path)
    jpg_file = message.json['photo'][2]['file_unique_id'] + '.jpg'
    open(jpg_file, 'wb').write(downloaded_photo)
    text_from_photo = image_recognizer.photo_2_text(jpg_file)
    os.remove(jpg_file)
    bot.send_message(message.from_user.id, text_from_photo)


@bot.message_handler(content_types=['audio'])
def handler_audio(message):
    bot.send_message(message.from_user.id, "audio")


@bot.message_handler(content_types=['voice'])
def handler_voice(message):

    tg_voice_msg = bot.get_file(message.voice.file_id)
    downloaded_voice = bot.download_file(tg_voice_msg.file_path)                # downloading file (voice) from telegram
    oga_file = message.json['voice']['file_unique_id'] + '.oga'
    open(oga_file, 'wb').write(downloaded_voice)                                    # write down voice into file (.ogg)

    wav_file = converter.oga_2_wav(oga_file)                                           # convert .oga to .wav

    text_from_voice = voice_recognizer.voice_2_text(wav_file)    # recognize the speech from .wav using "speech_recognition"

    os.remove(oga_file)
    os.remove(wav_file)
    bot.send_message(message.from_user.id, text_from_voice)                       # send the recognized text to the user


if __name__ == '__main__':
    bot.polling(none_stop=True)
