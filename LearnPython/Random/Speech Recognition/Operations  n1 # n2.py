import speech_recognition as sr


def sumAB(a, b):
    return a+b


def subAB(a, b):
    return a-b


def multiplyAB(a, b):
    return a*b


def divideAB(a, b):
    return a/b


def preprocess(number1, sign, number2):
    from word2number import w2n
    from googletrans import Translator

    translator = Translator()
    number1 = translator.translate(number1, dest='en', src='ro').text
    number2 = translator.translate(number2, dest='en', src='ro').text

    number1 = w2n.word_to_num(number1)
    number2 = w2n.word_to_num(number2)

    signs = {'plus': '+',
             'minus': '-',
             'înmulțit': 'x',
             'împărțit': '/'}

    sign = signs[sign]
    return number1, sign, number2


listener = sr.Recognizer()
while True:
    try:
        with sr.Microphone(device_index=18) as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language='ro-RO')
            print(info)

            number1, sign, number2 = info.split()
            number1, sign, number2 = preprocess(number1, sign, number2)
            result = 0
            # * two plus two
            # * doi plus doi
            if sign == '+':
                result = sumAB(number1, number2)
            # * two minus two
            if sign == '-':
                result = subAB(number1, number2)
            # * two multiply two
            if sign == 'x':
                result = multiplyAB(number1, number2)
            # * two divide two
            if sign == '/':
                result = divideAB(number1, number2)
            print(info, result)

    except Exception as e:
        print(e)
