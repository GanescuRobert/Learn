import speech_recognition as sr
listener = sr.Recognizer()

while True:
    try:
        with sr.Microphone(device_index=18) as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice,language='ro-RO')
            print(info)
    except Exception as e:
        print(e)