
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")
  
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname = ("Jarvis")
    speak("I am your Assistant")
    speak(assname)


def takeCommand():   
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak(f"Welcome, {uname}")
    # speak(uname)
    # columns = shutil.get_terminal_size().columns
     
    print("#####################")
    print(f"Welcome, {uname}")
    print("#####################")
     
    speak(f"How can I Help you {uname}?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()
    
# speak("hey my name is alexa")
# wishMe()
# username()  


if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    # username()
    
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")
        
        elif "open stackoverflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
            
        elif "play music" in query or "play song" in query:
            speak(f"playing your song {uname}")
            music_dir="C:/Users/aadib/Music"
            songs=os.listdir(music_dir)
            print(songs)
            random=os.startfile(os.path.join(music_dir, songs[1]))
        
        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"{uname}, the time is {strTime}")
            
        elif "send a mail" in query or "send an email" in query:
            try:
                speak("what should I say?")
                content= takeCommand()
                speak("whom should I send?")
                to=input()
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak(f"How are you, {uname}")
        
        elif "fine" in query or "good" in query:
            speak("It's good to know that you are fine")
        
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
            
        elif "what's your name" in query or "what is your name" in query:
            speak(f"my friends call me {uname}")
            print(f"my friends call me {uname}")
        
        elif f"exit {uname}" in query or f"quit {uname}" in query:
            speak("Thank you for your time")
            exit()
            
        elif "who made you" in query:
            speak("I have been created by Aaditya")
        
        elif "joke" in query:
            speak(pyjokes.get_joke())
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Aaditya. further It's a secret")
        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
            
        elif "power point" in query:
            speak("opening Power Point presentation")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
            os.startfile(power)
            
        elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
        
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "C:/Users/aadib/Desktop/Wallpapers/Naruto-HD-Wallpapers",
                                                       0)
            speak("Background changed successfully")
            
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
                
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
            
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
            
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
 
        elif "i love you" in query:
            speak("It's hard to understand")
            
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)

