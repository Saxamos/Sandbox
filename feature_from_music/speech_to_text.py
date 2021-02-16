import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('data/NISSAN/vocals.wav') as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text, language='fr-FR')
    print('Converting audio transcripts into text ...')
    print(text)
