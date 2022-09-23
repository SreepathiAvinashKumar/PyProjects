# import pyttsx3
# import pyaudio
# import speech_recognition as sr


# r = sr.Recognizer()
# initialize Text-to-speech engine
# engine = pyttsx3.init()

# # convert this text to speech
# text = "Python is a great programming language"
# engine.say(text)

# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[1].id)
# engine.say('The quick brown fox jumped over the lazy dog.')


# engine.startLoop(False)

# def externalLoop():
#     engine.iterate()
# # def onWord(name, location, length):
# #    print ('word', name, location, length)
# #    if location > 10:
# #       engine.stop()

# # engine.connect('started-word', onWord)

# engine.runAndWait()


# with sr.Microphone() as source:
#     # read the audio data from the default microphone
#     audio_data = r.record(source, duration=5)
#     print("Recognizing...")
#     # convert speech to text
#     text = r.recognize_google(audio_data)
#     print(text)
