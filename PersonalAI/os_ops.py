import os
import subprocess as sp
from tokenize import Special
import wikipedia
import random
import pyttsx3
from datetime import datetime as dt
import speech_recognition as sr
import os_ops as ops
import pyjokes

# USER_NAME = getpass.getuser()

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

extra_information = [

    ""
]

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'vscode': "C:\\Users\\sripa\\AppData\Local\\Programs\\Microsoft VS Code\\code.exe",
    'Android_studio': "C:\\Users\\sripa\\Desktop\\AndroidStudio.lnk",
    'wordpad':"C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
}


def say_hello():
    speak("Hello Sir, How are You ?")


def open_vscode():
    os.startfile(paths['vscode'])


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

# def open_notepad():
#     os.startfile(paths['notepad'])


def open_android_studio():
    print("working")
    os.startfile(paths['Android_studio'])


def open_calculator():
    os.startfile(paths['calculator'])


def open_wordpad():
    os.startfile(paths['wordpad'])

def open_cmd():
    os.system('start cmd')


def open_filemanger():
    os.system("start explorer")


def search_on_wikipedia(query):
    ops.speak(wikipedia.summary(query, sentences=2))
    ops.speak("For your convenience, I am printing it on the screen sir.")
    print(wikipedia.summary(query, sentences=5))


hour = dt.now().hour

engine = pyttsx3.init("sapi5")

engine.setProperty('rate', 150)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# def greet():
#     if (hour > 6) and (hour <= 12):
#         speak(f"good Morning{os.getlogin()}")
#         print(os.getlogin())
#     elif (hour >= 12) and (hour <= 16):
#         print(os.getlogin())
#         speak(f"good Afternoon{os.getlogin()}")
#     elif (hour > 16) and (hour <= 19):
#         speak(f"good Evening{os.getlogin()}")
#         print(os.getlogin())
#     else:
#         print("Good Night")


def current_date():
    date = dt.now().date()
    speak(f"Today's date is {date}")


def current_day():
    dtime = dt.now()
    day = dtime.strftime("%A")
    speak(f"today is {day} Sir")


def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        Query = r.recognize_google(audio, language='en-in')
        print(Query)
        # if not 'exit' in query or 'stop' in query:
        #     speak(choice(opening_text))
        # else:
        #     greet()
        return Query
    except Exception:
        print("Sorry Did'nt Understand")
        a = random.randint(0, 2)
        speak(opening_text[a])
        query = None
        return query

def time():
    now = dt.now()
    current_time = now.strftime("%H:%M")
    speak(f"time is {current_time} sir")


def tell_joke():
     joke = pyjokes.get_joke()
     print(joke)
     speak(joke)




# def add_to_startup(file_path=""):
#     if file_path == "":
#         file_path = os.path.dirname(os.path.realpath(__file__))
#     bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
#     with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
#         bat_file.write(r'start "" "%s"' % file_path)

