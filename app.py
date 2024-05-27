from engine import *
from command import takeCommand
from playsound import playsound
import os
from youtube import searchYoutube
from gSearch import searchGoogle
from event import mycursor
import re

# count = 2
# while count >= 0:
#     speak("Enter Password")
#     print("Enter Password")
#     a = input()
#     pw_file = open("pass.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if (a==pw):
#         speak("Access Granted.")
#         playsound('sound\Windows Logon.wav')
#         break
#     elif count != 0 and a != pw:
#         speak("Access Denied.")
#         speak(f"You have {count} more chance.")
#         count = count-1
#     else:
#         playsound('sound\Windows Error.wav')
#         speak("Please Try Again Later.")
#         exit()



while True:
    query = takeCommand().lower()


    if "shutdown" in query:
        speak("Ok sir, have a nice day.")
        playsound("sound\Windows Logoff Sound.wav")
        break
    
    elif 'open' in query:
        speak('Launching, Sir...')
        query = query.replace("open", "")
        os.system(f"start {query}")

    elif "google" in query:
        searchGoogle(query)

    elif "youtube" in query:
        searchYoutube(query)
   
    elif "remember that" in query:
        rememberMessage = query.replace("remember that","")
        speak("You told me to "+rememberMessage)
        remember = open("Remember.txt","a")
        remember.write(rememberMessage)
        remember.close()

    elif "what do you remember" in query:
        remember = open("Remember.txt","r")
        if os.path.getsize("Remember.txt") != 0:
            speak("You told me to" + remember.read())
        else:
            speak("Sir, you didn't tell me anything nothing new and you have erased my previous memory.")

    elif "forget what you remember" in query:
        remember = open("Remember.txt","r+")
        remember.truncate(0)
        remember.close()
        speak("Ok Sir, memory erased.")

    elif "speak the text" in query:
        speak("Enter the text")
        text = input()
        speak(text)
    
    elif "note topics for today" in query:
        speak("What are the topics")
        topics = takeCommand().lower()
        topic_list = topics.split(' ')
        notes = open("note.txt","a")
        for points in topic_list:
            notes.write(f'{points}\n')
        notes.close()
    
    elif 'what are the topics' in query:
        notes = open("note.txt", 'r')
        lines = notes.readlines()
        speak('Sir, the topics for today are  ')
        for line in lines:
            speak(line)
        notes.close()
    
    elif 'list all professions from new event' in query:
        mycursor.execute ('select distinct profession from new')
        professions = mycursor.fetchall()
        speak("here is a list of all the professions from new event")
        for profession in professions:
            speak(f'{profession}')
    
 
    elif re.search(r'list (\w+.\w*) from (\w+) event', query):
        query = query.replace("list", "")
        query = query.replace(" from", "")
        query = query.replace(" event", "")
        query = query.strip()
        search = query.split(' ')
        profession = ' '.join(search[:len(search)-1])
        event = search[-1]
        print(profession, event)
        # profession = 'software engineer'
        # event = 'new'
        speak(f'Here is a list of {profession} from {event} event')
        mycursor.execute(f"Select name, email, mobile from {event} where profession= '{profession}'")
        data = mycursor.fetchall()
        for name, email, mobile in data:
            speak(f'{name} is a {profession} and his contact details are') 
            speak(f'email ID {email}')  
            speak(f'mobile number {mobile}')

    else:
        speak(query)