import warnings
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import webbrowser
import os 
import time
from pyautogui import click
from keyboard import press,write
from time import sleep
import eel
eel.init("project")



warnings.filterwarnings("ignore")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #changing index , changes voices, 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio)
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I can't understand what you mean"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def today_date():
    now = datetime.datetime.now()
    return now 


def wiki(text):
    text = text.replace("wikipedia"," ")
    text = text.replace("Vaibhav Assistant"," ")
    results = wikipedia.summary(text , sentences=3)
    return results

def WhatsappMsg(name,message):
     
    webbrowser.open("https://web.whatsapp.com/")

    sleep(15)

    buttonlocation = pyautogui.locateOnScreen('search.png')
    buttonpoint = pyautogui.center(buttonlocation)
    buttonx, buttony = buttonpoint
    click(buttonx,buttony)

    sleep(1)

    write(name)

    sleep(2)
    
    buttony+=150
    click(buttonx,buttony)
    
    sleep(0.5)

    butlocation = pyautogui.locateOnScreen('newss.png')
    butpoint = pyautogui.center(butlocation)
    butx, buty = butpoint
    click(butx,buty)
    

    sleep(0.5)

    write(message)

    press('enter')



def WhatsappChat(name):

    webbrowser.open("https://web.whatsapp.com/")

    sleep(10)

    buttonlocation = pyautogui.locateOnScreen('search.png')
    buttonpoint = pyautogui.center(buttonlocation)
    buttonx, buttony = buttonpoint
    click(buttonx,buttony)

    sleep(1)

    write(name)

    sleep(2)

    buttony+=150
    click(buttonx,buttony)

    sleep(0.5)

    butlocation = pyautogui.locateOnScreen('msg.png')
    butpoint = pyautogui.center(butlocation)
    butx, buty = butpoint
    click(butx,buty)
    
    sleep(0.5)


@eel.expose
def trail():
    talk("Hello this is Vaibhav Assistant , the virtual assisstant")
    while True:
        text = get_audio()
        speak = " "
        if "time" in text:
            X = today_date()
            eel.addText(X)
            speak = speak + str(X)
                    
        elif "wikipedia" in text or "Wikipedia" in text:
            results = wiki(text)
            speak = speak + results
            eel.addText(results)
                    
    
        elif "who are you" in text or "define yourself" in text:
            speak = speak + """Hello, I am Vaibhav Assistant, created by Gopi Vaibhav"""
            
        elif "your name" in text:
            speak = speak + "This is Vaibhav Assistant."
    
        elif "who am i" in text:
            speak = speak + "You might be a human."
            
        elif "why do you exist" in text or "why did you come" in text:
            speak = speak + "It is a secret."
    
        elif "how are you" in text:
            speak = speak + "I am fine, Thank you!"
            speak = speak + "\nHow are you?"
                    
        elif "i am good" in text or "i am fine" in text:
            speak = speak+ "cool , How can i help for you"
                    
        elif "i am fine" in text :
            speak = speak + "It's good to know that you are fine"
                    
            
        elif "open" in text.lower():                
            if "browser" in text.lower():
                speak = speak + "opening default browser"
                os.startfile(
                    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
                    )

            elif "word" in text.lower():
                speak = speak + "opening Microsoft word document"
                os.startfile(
                    r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )
            elif "youtube" in text.lower():
                speak = speak + "opening youtube in browser"
                webbrowser.open("https://youtube.com/")
            
            elif "facebook" in text.lower():
                speak = speak + "opening facebook in browser"
                webbrowser.open("https://www.facebook.com/")

            elif "instagram" in text.lower():
                speak = speak + "opening instagram in browser"
                webbrowser.open("https://www.instagram.com/")
                
            elif "google" in text.lower():
                speak = speak + "opening google in browser"
                webbrowser.open("https://google.com")
            
            elif "whatsapp" in text.lower():
                speak = speak + "opening whatsapp in browser"
                webbrowser.open("https://web.whatsapp.com/")
                
            elif "github" in text.lower():
                speak = speak + " opening github"
                webbrowser.open("https://github.com")
                
            else:
                    speak = "No such Application in framework "
                
            #searching something on browser
        elif "youtube" in text.lower():
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
            speak = speak +"opening" + str(search) +  " on youtube "
                        
        elif "search" in text.lower():
            x = text.lower().split().index("search")
            y = text.split()[x + 1:]
            webbrowser.open("https://www.google.com/search?q="+"+".join(y))    
            speak = speak +"searching" + str(y) + " on browser"
            
                
        elif "where is" in text:
            a =  text.lower().split().index("is")
            location = text.split()[a +1: ]
            webbrowser.open("https://www.google.com/maps/place/"+"+".join(location))
                        
        elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
            talk("for how many seconds do you want me to sleep")
            a = int(get_audio())
            time.sleep(a)
            speak = speak + str(a) + " seconds completed. Now you can ask me anything"
                    
        elif "whatsapp" in text :
            if "message" in text:
                talk("What's the name of reciever")
                name = get_audio()
                talk("What's the message you wanna send")
                message = get_audio()
                WhatsappMsg(name,message)
                break

            if "chat" in text:
                talk("Whats the name of chat")
                name = get_audio()
                talk("Opening chat")
                WhatsappChat(name)
                break
                
        elif "goodbye" in text or "bye" in text or "quit" in text or "exit" in text:
            talk("Terminating Vaibhav Assistant")
            break 
        talk(speak)
        eel.addText("Vaibhav Assistant : "+speak)


eel.start("project.html",size=(500, 500))