import speech_recognition as sr


def voice_2_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = 'can`t recognize'
    return text
