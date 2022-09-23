import random as r
from re import search
import pyttsx3
from datetime import datetime as dt
# import os
import speech_recognition as sr
import os_ops as ops
# import wikipedia
import webbrowser

# term = "radio"
# webbrowser.open(f"https://www.google.com/search?q={term}")

ASSISTANT_NAME = "Aiden"

if __name__ == '__main__':
    ops.say_hello()
    # ops.greet()

    while True:
        try:
            query = ops.take_user_input().lower()
            if 'open notepad' in query:
                ops.open_notepad()
                continue
            elif 'open android studio' in query:
                ops.open_android_studio()

            elif 'open command prompt' in query or 'open cmd' in query:
                ops.open_cmd()
                continue

            elif 'tell me the time' in query:
                ops.time()
                continue
            
            elif 'tell me a joke' in query:
                ops.tell_joke()
                continue

            elif "what is today's date" in query:
                ops.current_date()
                continue
            elif "what is today's day" in query:
                ops.current_day()
                continue
            # elif "how are you" in query:
            #     ops.speak("I am fine What about You Sir")
            #     continue
            elif 'open vs code' in query:
                ops.open_vscode()
                continue
            elif 'open camera' in query:
                ops.open_camera()
                continue
            elif 'open calculator' in query:
                ops.open_calculator()
                continue
            elif 'wikipedia' in query:
                ops.speak('What do you want to search on Wikipedia,Sir?')
                search_query = ops.take_user_input().lower()
                ops.search_on_wikipedia(search_query)
                continue
            elif 'stop' in query or 'end the session ' in query or 'close the session' in query:
                ops.speak("I am Closing the session sir")
                exit()
            elif 'youtube channel' in query:
                search_array = query.split()
                print(query)
                term = search_array[0] + search_array[1]
                webbrowser.open(f"https://www.youtube.com/search?q={term}")
                continue
            elif 'tell me about' in query:
                search_a = query.split()
                ops.search_on_wikipedia(search_a[3])
                continue
            elif 'open wordpad' in query:
                ops.open_wordpad()
                continue
            elif 'how are you' in query:
                li = ['good', 'fine', 'great']
                choice_li = r.choice(li)
                print(choice_li)
                ops.speak(f"I am {choice_li} sir")
                continue
            elif 'who are you' in query or 'what is your name' in query:
                print(ASSISTANT_NAME+"..")
                ops.speak(f"This is {ASSISTANT_NAME} Sir")
                continue
            elif 'play' in query:
                search_array = query.split()
                print(query)
                term = search_array[1]+" "+search_array[2]
                print(term)
                webbrowser.open(f"https://www.jiosaavn.com/search/{term}")

            elif 'open file manager' in query:
                ops.open_filemanger()
                continue

        except KeyboardInterrupt:
            print("Personal Assisstant Stopped")
            exit()
        except Exception:
            continue
