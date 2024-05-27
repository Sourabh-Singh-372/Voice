from engine import *
import pywhatkit

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("L", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("No speakable output available")