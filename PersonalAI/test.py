from queue import Empty
from weakref import ReferenceType
import keyboard
import os_ops as ops
import random as r
import os
import psutil
from pytube import YouTube
import requests
import subprocess
from bs4 import BeautifulSoup


# keyboard.wait("a")
# # keyboard.write("\n The key 'a' was pressed!")
# print("a is pressed")

# keyboard.wait("e")
# print("e is pressed")

# keyboard.wait("i")
# print("i is pressed")

# keyboard.wait("o")
# print("o is pressed")

# keyboard.press_and_release('R, K')

# keyboard.wait("a")
# if keyboard.is_pressed("a"):
#     print("a pressed")


# keyboard.press_and_release('shift+s')


# query = ops.take_user_input().lower()

# d = os.startfile("C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe")

# keyboard.press_and_release('alt+tab')


# while True:
#     try:
#         txt = ops.take_user_input()
#         keyboard.write(txt)
#     except Exception:
#         ops.speak("Tell Something")
#         continue
#     except KeyboardInterrupt:
#         print("Session Closed")
#         break

# recorded = keyboard.record(until='esc')




# Then replay back at three times the speed.

# keyboard.play(recorded, speed_factor=3)

# link = input("Youtube Link:")
# yt = YouTube(link)
# file_name = 'Hello.txt'


# subprocess.Popen(["C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"])



# keyboard.write("Hleoooo")    

# qu = "samajavargamana+song"

# r = requests.get(f"https://www.youtube.com/results?search_query={qu}")
# soap = BeautifulSoup(r.content,'html.parser')
# print(soap.prettify())