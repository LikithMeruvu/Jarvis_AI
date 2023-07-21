# import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as pwt
import webbrowser as wb
import os
import random
import datetime
from bardapi import Bard


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(data):
    engine.say(data)
    engine.runAndWait()


def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-us ')
        print(f"You said: {query}")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        # speak("Say that again please")   #Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


def wish_me(greet="jarvis Here, how can i help you"):
    time = (datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Hi, Good morning")
    elif time >= 12 and time < 18:
        speak("Hi, Good afternoon")
    else:
        speak("hi, good evening")
    speak(greet)


def get_info_from_wikipedia(query: str, lines: int):
    speak("searching wikipedia")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=lines)
    print(results)
    speak(results)


def Open_Google(query: str):
    speak("opening google")
    li = query.split(" ")
    i = li.index("google")
    res = li[i+3:len(li)]
    query = ' '.join([str(elem) for elem in res])
    print(query)
    pwt.search(query)


def Open_YouTube(query: str):
    speak("opening youtube")
    # query = query.replace("open youtube", "")
    li = query.split(" ")
    i = li.index("youtube")
    res = li[i+3:len(li)]
    query = ' '.join([str(elem) for elem in res])
    print(query)
    pwt.playonyt(query)


def Play_music():
    songs_path = os.getcwd() + '\Music'
    songs = os.listdir(songs_path)
    os.startfile(os.path.join(
        songs_path, songs[random.randrange(0, len(songs))]))


def Open_Code():
    codepath = "C:\\Users\\91630\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
    speak("opening v s code")
    os.startfile(codepath)

def Ask_Bard(Query):
   token = 'ZAiKGeBg0eL15j1vGK6jFzU4V46aODCCa-3LyqwSLpGHbPYDqGtDuVkFlkZ1knOnpPYZEA.'
   bard = Bard(token=token)
   response = bard.get_answer(Query)['content']
   print(response)
   speak(response)




def WhatsApp():
    speak("For Whom should i send message")
    Contacts = {
        'mom': 789XXXXXXX,
        'friend': 756XXXXXXX,
        'me': 810XXXXXXX,
        'jay': 996XXXXXXX,
        'tory' : 92XXXXXXX 
    }
    to = takeCommand()
    speak("what message should i send")
    msg = takeCommand()
    speak(f"sending message to {to}")
    try:
        # change your phone country code mine is +91
        pwt.sendwhatmsg_instantly(f"+91{Contacts[to]}", msg)
    except Exception as e:
        speak("error sending message")
        print(e)


if __name__ == '__main__':
    wish_me()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            get_info_from_wikipedia(query, 5)

        # say :- open youtube and play {Your desired song}
        elif 'open youtube' in query:
            Open_YouTube(query)

        elif 'open google' in query:
            Open_Google(query)

        elif 'online code' in query:
            speak("opening repell")
            wb.open('replit.com/@meruvulikith')

        elif 'play music' in query:
            Play_music()

        elif 'open code' in query:
            Open_Code(query)

        elif 'whatsapp message' in query:
            WhatsApp()

        elif 'exit' in query:
            speak("have a good day mate, see you later")
            exit()

        else:
            Ask_Bard(query)
