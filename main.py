import speech_recognition as sr
import os
import win32com.client
import webbrowser
# import openai
import datetime


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 500
        audio = r.listen(source) #Starts Listening
        print("Thanks")
    try:
        text = r.recognize_google(audio, language = "en-in") #Recognizes audio in English 
        print(text)
        return text
    except Exception as e: #When there is no notable speech
        return "Sorry, couldn't hear you!"

        
if __name__ == "__main__":    
    # print("Enter the word")
    say("Hello, I am JARVIS AI")
    while True:      
        query = takeCommand()
        #todo: Add more sites
        sites = [["youtube", "http://www.youtube.com"], ["instagram", "http://instagram.com"]]
        for site in sites:                    
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} for you")
                webbrowser.open(site[1])
        #todo: add a feature to play a specific song
        if "open word" in query.lower():
            word_path = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk"
            os.system(f"{word_path}")
        if "the time" in query.lower():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strftime}")                
                
                

                
