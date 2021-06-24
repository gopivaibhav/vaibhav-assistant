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
import speedtest
import eel
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
            talk(x)
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

def trans():
    translator = Translator(service_urls=['translate.googleapis.com'])
    talk("what to translate")
    trans_ = get_audio_hindi()
    results = translator.translate(trans_)
    Text = results.text
    return Text

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

def SpeedTest():
    talk("Checking speed")
    st = speedtest.Speedtest()
    st.get_best_server()
    downloding = st.download()
    correctDown = downloding/800000
    uploading = st.upload()
    correctUp = uploading/800000
    eel.addText("Downloading Speed : "+str(correctDown)[:5]+" MB")
    eel.addText("Uploading Speed : "+str(correctUp)[:5]+" MB")
    return "Here are the results of your internet speed"

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
                    
    
        elif "who are you" in text or "define yourself" in text:
            speak = "Hello, I am Vaibhav Assistant, created by Gopi Vaibhav"
            
        elif "your name" in text:
            speak = "This is Vaibhav Assistant."
    
        elif "who am i" in text:
            speak = "You might be a human."
            
        elif "why do you exist" in text or "why did you come" in text:
            speak = "It is a secret."
    
        elif "how are you" in text:
            speak =  "I am fine, Thank you!"
            speak += "\nHow are you?"
                    
        elif "i am good" in text or "i am fine" in text:
            speak  ="cool , How can i help for you"
                    
        elif "i am fine" in text :
            speak = "It's good to know that you are fine"
                    
            
        elif "open" in text.lower():                
            if "youtube" in text.lower():
                speak = "opening youtube in browser"
                webbrowser.open("https://youtube.com/")
            
            elif "facebook" in text.lower():
                speak = "opening facebook in browser"
                webbrowser.open("https://www.facebook.com/")

            elif "instagram" in text.lower():
                speak = "opening instagram in browser"
                webbrowser.open("https://www.instagram.com/")
                
            elif "google" in text.lower():
                speak = "opening google in browser"
                webbrowser.open("https://google.com")
            
            elif "whatsapp" in text.lower():
                speak = "opening whatsapp in browser"
                webbrowser.open("https://web.whatsapp.com/")
                
            elif "github" in text.lower():
                speak = " opening github"
                webbrowser.open("https://github.com")
                
            else:
                    speak = "No such Application in framework "
                
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
            talk("What's the location?")
            eel.addText("What's the location?")
            Location = get_audio()
            weather(Location)
            speak = 'Here are the weather reports of '+str(Location)    
                        
        elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
            talk("for how many seconds do you want me to sleep")
            a = int(get_audio())
            time.sleep(a)
            speak = str(a) + " seconds completed. Now you can ask me anything"
        
        elif "hindi" in text or "translate" in text:
            speak=trans()
        
        elif "speed" in text:
            speak=SpeedTest()

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
            talk("Terminating Vaibhav Assistant")
            break 
        
        eel.addText("Vaibhav Assistant : "+speak)
        talk(speak)
        


eel.start("project.html",size=(500, 500))