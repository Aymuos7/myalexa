import speech_recognition as paanji
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = paanji.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cd():
    try:
        with paanji.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'alexa' in cmd:
                cmd = cmd.replace('alexa', '')
                print(cmd)
    except:
        pass
    return cmd


def run_alexa():
    cmd = take_cd()
    if 'play' in cmd:
        song = cmd.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in cmd:
        per = cmd.replace('who is', '')
        info = wikipedia.summary(per, 2)
        print(info)
        talk(info)
    elif 'joke' in cmd:
        jo = pyjokes.get_joke()
        talk(jo)
        print(jo)
    else:
        talk('plz say the command again.')

while True:
    run_alexa()

