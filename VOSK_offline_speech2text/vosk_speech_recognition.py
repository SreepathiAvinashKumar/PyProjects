import pyaudio
from vosk import Model,KaldiRecognizer
import pyttsx3


engine = pyttsx3.init("sapi5")

engine.setProperty('rate', 150)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    model = Model("./vosk-model-small-en-in-0.4")
    recoginizer  = KaldiRecognizer(model,16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(rate=16000,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=8192)
    stream.start_stream()

    while True:  
     try:
        data= stream.read(8192)
        if recoginizer.AcceptWaveform(data):
            d = recoginizer.Result()[14:-3]
            # speak(d)
            return d 
     except Exception:
       continue
     except Exception:
       break
