
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import random
import pywhatkit as pwt
import google.generativeai as genai # Import GeminiPro from gemini_pro module
from dotenv import load_dotenv  # Import load_dotenv from dotenv module

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('GEMINI_PRO_API_KEY')

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

# Function to speak out the data


def speak(data):
    engine.say(data)
    engine.runAndWait()

# Function to take user command via microphone input


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
        query = r.recognize_google(audio,language='en-us')
        print(f"You said: {query}")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        # speak("Say that again please")   #Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


# Function to greet the user based on the time of day


def wish_me(greet="jarvis Here, how can i help you"):
    time = (datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak("Hi, Good morning")
    elif time >= 12 and time < 18:
        speak("Hi, Good afternoon")
    else:
        speak("hi, good evening")
    speak(greet)

# Function to get information from Wikipedia based on user query


def get_info_from_wikipedia(query: str, lines: int):
    speak("searching wikipedia")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=lines)
    print(results)
    speak(results)

# Function to open Google search based on user query


def Open_Google(query: str):
    speak("opening google")
    li = query.split(" ")
    i = li.index("google")
    res = li[i+3:len(li)]
    query = ' '.join([str(elem) for elem in res])
    print(query)
    pwt.search(query)

# Function to open YouTube and play a specific song based on user query


def Open_YouTube(query: str):
    speak("opening youtube")
    li = query.split(" ")
    i = li.index("youtube")
    res = li[i+3:len(li)]
    query = ' '.join([str(elem) for elem in res])
    print(query)
    pwt.playonyt(query)

# Function to play random music from a specified directory


def Play_music():
    songs_path = os.getcwd() + '\Music'
    songs = os.listdir(songs_path)
    os.startfile(os.path.join(
        songs_path, songs[random.randrange(0, len(songs))]))

# Function to open Visual Studio Code application


def Open_Code():
    codepath = "C:\\Users\\91630\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
    speak("opening v s code")
    os.startfile(codepath)

# Function to interact with Gemini Pro API for answering queries


genai.configure(api_key = API_KEY)
def Ask_GeminiPro(Query):
    speak("Searching Internet wait for a second")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(Query)
    print(response.text)
    speak(response.text)

# Function to send WhatsApp messages to specified contacts


def WhatsApp():
    speak("For Whom should i send message")

    Contacts = {
        'mom': 789345734857,
        'friend': 756345734857,
        'me': 810345734857,
        'jay': 996345734857,
        'tory': 92345734857
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
            Open_Code()

        elif 'whatsapp message' in query:
            WhatsApp()

        elif 'exit' in query:
            speak("have a good day mate, see you later")
            exit()

        elif 'jarvis' in query:
            Ask_GeminiPro(query)
