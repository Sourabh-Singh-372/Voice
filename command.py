import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n ")
    except Exception as e:
        print(e)

        print("Sorry I didn't recognise that.")
        return "Sorry I didn't recognise that."
    return query
