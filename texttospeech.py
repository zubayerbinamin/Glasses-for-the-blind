import pyttsx3
engine = pyttsx3.init()

def say(speech):
    engine.say(speech)
    engine.runAndWait()
    

say("Hello")
