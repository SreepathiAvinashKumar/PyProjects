import vosk_test as vt 

while True:
  try:
   d = vt.listen()
   vt.speak(d)
  except Exception:
    vt.speak("Ask Me")
    continue
  except KeyboardInterrupt:
    print("Session Stopped")
    break
