import warnings
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import requests
from pyautogui import click, keyDown, keyUp
from keyboard import press,write
from time import sleep
from googletrans import Translator
from PyDictionary import PyDictionary
import eel
import random
import os
eel.init("project")


warnings.filterwarnings("ignore")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  #changing index , changes voices, 1 for female and 0 for male

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk('Speak now')
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio)
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def today_date():
    date = str(datetime.datetime.now().date())
    hour = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)
    sec = str(datetime.datetime.now().second)
    time=date+" "+hour+"hours "+min+"minutes "+sec+"seconds"
    return time

def get_audio_telugu():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk("Speak now")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio,language='te-IN')
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def get_audio_hindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        eel.addText("Listening....")
        talk("Speak now")
        audio = r.listen(source)
        try:
            global speech
            speech=" "
            speech = r.recognize_google(audio,language='hi')
            speech = speech.lower()
            eel.addText("You said: "+speech)
        except sr.UnknownValueError:
            x = "Sorry,I couldn't hear you"
            talk(x)
            eel.addText(x)
        except sr.RequestError:
            talk("Sorry , My API to recognize voice is down")
    return speech

def trans_hindi():
    translator = Translator(service_urls=['translate.googleapis.com'])
    eel.addText("Vaibhav Assistant : What should I translate")
    talk("what Should I translate")
    trans_ = get_audio_hindi()
    results = translator.translate(trans_)
    Text = results.text
    return Text+" is the translated text"

def trans_telugu():
    translator = Translator(service_urls=['translate.googleapis.com'])
    eel.addText("Vaibhav Assistant : What should I translate")
    talk("what Should I translate")
    trans_ = get_audio_telugu()
    results = translator.translate(trans_)
    Text = results.text
    return Text+" is the translated text"

def coin_toss():
    eel.addText("Vaibhav Assistant : I am going to flip coin......!")
    talk("I am going to flip coin")
    result = random.choice(["Heads","Tails"])
    return result

def weather(location):
    user_api =  "551fa158b9c984913a5f0b943e7e8578"
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = str(api_data['main']['humidity'])
    wind_spd = str(api_data['wind']['speed'])
    date = str(datetime.datetime.now().date())
    eel.addText("Weather Stats for - "+date)
    eel.addText("Current temperature is: {:.2f} deg C".format(temp_city))
    eel.addText("Current weather desc  :"+weather_desc)
    eel.addText("Current Humidity in %     :"+hmdt)
    eel.addText("Current wind speed  in kmph :"+wind_spd)
    return temp_city

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

@eel.expose
def trail():
    eel.addText("Hello this is Vaibhav Assistant , the voice assisstant")
    talk("Hello this is Vaibhav Assistant , the voice assisstant")
    while True:
        text = get_audio()
        speak = "Sorry, I don't have reply for this"

        if "time" in text:
            X = today_date()
            speak = X
                    
        elif "wikipedia" in text or "Wikipedia" in text:
            results = wiki(text)
            speak =results
                    
    
        elif "who are you" in text:
            speak = "Hello, I am Vaibhav Assistant, created by Gopi Vaibhav"
            
        elif "your name" in text:
            speak = "This is Vaibhav Assistant."
    
        elif "who am i" in text:
            speak = "You are a Human"
            
        elif "why are you here" in text or "why did you come" in text:
            speak = "Because you activated me."
    
        elif "how are you" in text:
            speak =  "I am fine, Thank you!"
            speak += "\nWhat about you?"
                    
        elif "i am good" in text or "i am fine" in text or "i am nice" in text:
            speak  ="cool , How can i help for you"
            
        elif "open" in text.lower():                
            if "whatsapp" in text.lower():
                speak = "opening whatsapp web in browser"
                webbrowser.open("https://web.whatsapp.com/")
                
            else:
                l=text.lower().split('open ')
                webbrowser.open("https://"+l[1]+".com")
                speak = " opening "+l[1]+" in browser"
                
        elif "youtube" in text.lower():
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            webbrowser.open("https://www.youtube.com/results?search_query=" + "+".join(search))
            speak ="opening" + str(search) +  " on youtube "
                        
        elif "search" in text.lower():
            x = text.lower().split().index("search")
            y = text.split()[x + 1:]
            webbrowser.open("https://www.google.com/search?q="+"+".join(y))    
            speak ="searching" + str(y) + " on google"
            
                
        elif "where is" in text:
            a =  text.lower().split().index("is")
            location = text.split()[a +1: ]
            speak ="searching for "+str(location)
            webbrowser.open("https://www.google.com/maps/place/"+"+".join(location))

        elif "weather" in text or "climate" in text:
            eel.addText("What's the location?")
            talk("What's the location?")
            Location = get_audio()
            weather(Location)
            speak = 'Here are the weather reports of '+str(Location)    
                        
        elif "don't listen" in text or "do not listen" in text:
            eel.addText("Vaibhav Assistant : How many seconds do you want me to sleep")
            talk("How many seconds do you want me to sleep?")
            a = int(get_audio())
            time.sleep(a)
            speak = str(a) + " seconds completed. Now you can ask me anything"
        
        elif "translate" in text:
            eel.addText("Vaibhav Assistant : What is the language you are going to speak?")
            talk("What is the language you are going to speak?(Hindi or Telugu)")
            lang = get_audio()
            lang = lang.lower()
            if "hindi" in lang:
                speak=trans_hindi()
            else:
                speak=trans_telugu()
        
        elif "meaning" in text:
            dictionary=PyDictionary()
            l=text.split(' of ')
            meaningword=l[1]
            out = dictionary.meaning(meaningword)
            eel.addText("Vaibhav Assistant : Meaning of "+l[1]+" is "+str(out))
            talk("Meaning of "+l[1]+" is "+str(out))

        elif "synonym" in text:
            dictionary=PyDictionary()
            l=text.split(' of ')
            synonymword=l[1]
            out = dictionary.synonym(synonymword)
            eel.addText("Vaibhav Assistant : Synonyms of "+l[1]+" are "+str(out))
            talk("Synonyms of "+l[1]+" are "+str(out))

        elif "antonym" in text:
            dictionary=PyDictionary()
            l=text.split(' of ')
            antonymword=l[1]
            out = dictionary.antonym(antonymword)
            eel.addText("Vaibhav Assistant :  Antonyms of "+l[1]+" are "+str(out))
            talk("Antonyms of "+l[1]+" are "+str(out))

        elif "toss" in text or "flip" in text:
            speak=coin_toss()
            

        elif "shutdown" in text :
            eel.addText("Vaibhav Assistant : Would you like to shutdown PC?")
            talk("Would you like to shutdown PC")
            shutdown = get_audio()
  
            if shutdown == 'no':
                eel.addText("Vaibhav Assistant : Request Cancelled")
                talk("request cancelled")
                exit()
            else:
                talk("Shutting down PC")
                os.system("shutdown /s /t 1")
        
        elif "restart" in text:
            eel.addText("Vaibhav Assistant : Would you like to restart PC?")
            talk("Would you like to restart PC")
            restart = get_audio()
  
            if restart == 'no':
                eel.addText("Vaibhav Assistant : Request Cancelled")
                talk("request cancelled")
                exit()
            else:
                talk("Shutting down PC")
                os.system("shutdown /r /t 1")

        elif "whatsapp" in text :
            if "message" in text:
                eel.addText("What's the name of person?")
                talk("What's the name of person")
                name = get_audio()
                eel.addText("What's the message you wanna send?")
                talk("What's the message you wanna send")
                message = get_audio()
                talk("Opening whatsapp web")
                WhatsappMsg(name,message)
                break

            if "chat" in text:
                eel.addText("What's the name of person?")
                talk("What's the name of person")
                name = get_audio()
                talk("Opening chat")
                WhatsappChat(name)
                break
                
        elif "goodbye" in text or "bye" in text or "quit" in text or "exit" in text:
            eel.addText("Terminating Vaibhav Assistant")
            talk("......Terminating Vaibhav Assistant......")
            break 
        
        eel.addText("Vaibhav Assistant : "+speak)
        talk(speak)
        


eel.start("project.html",size=(1000, 1000))