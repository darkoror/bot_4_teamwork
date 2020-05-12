import speech_recognition as sr


def voice_2_en(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = 'can`t recognize'
    return text


def voice_2_ru(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_wit(audio_data=audio, key='BTSXQDFI5VXYM575B7UKNT65DLETMFW6')#, language='ru-RU')
        except:
            text = 'can`t recognize'
    return text


def voice_2_ukr(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_wit(audio_data=audio, key='CKVFQQNDSWZYVUVRV6IZR37O2IQVNV3O')
        except:
            text = 'can`t recognize'
    return text
