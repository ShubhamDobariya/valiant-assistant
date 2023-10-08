import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import datetime



Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty('rate',150)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"{audio}")
    Assistant.runAndWait()


def TakeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Lintening....")
        command.pause_threshold = 1
        audio = command.listen(source)
        
        
        
        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said : {query}")
            
            
        except Exception as Error:
            return "none"
        
        return query.lower()
    
    
        
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        Speak("Good morning!")
    elif hour>12 and hour<=18:
        Speak("Good afternoon!")
    else:
        Speak("Good evening!")

    Speak("I am valiant A I, How can I help you ? ")    
    
    
def Task():
    
    
    
    while True:
        
        
        query = TakeCommand()

        
        if 'hello' in query:
            Speak("Hello,sir")
            Speak("How can I help you")
            
        elif 'what is your name' in query:
            Speak("I am valiant A I")
            
        elif 'How are you' in query:
            Speak("I am Fine sir")
            Speak("whats about you")
            
        elif 'by' in query:
            Speak("ok sir, Bye")
            break
        
        elif 'youtube search' in query:
            # Speak("Ok,sir  What should you search on youtube")
            query = query.replace("valiant","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done,sir")
            
        elif 'google search' in query:
            # Speak("Ok,sir  What should you search on Google")
            query = query.replace("valiant","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done,sir")
            
        # elif 'website' in query:
        #     Speak("Ok,sir")
        #     query = query.replace("jarvis","")
        #     query = query.replace("website","")
        #     web1 = query.replace("open","")
        #     web2 = 'https://www.' + web1 + '.com'
        #     webbrowser.open(web2)
        #     Speak("Done,sir")
            
        elif 'facebook' in query:
            Speak("Ok,sir")
            webbrowser.open('https://www.facebook.com/')
            Speak("Done,sir")
        
        elif 'instagram' in query:
            Speak("Ok,sir")
            webbrowser.open('https://www.instagram.com/')
            Speak("Done,sir")   

        elif 'linkedin' in query:
            Speak("Ok,sir")
            webbrowser.open('https://www.linkedin.com/')
            Speak("Done,sir")
            
        elif 'twitter' in query:
            Speak("Ok,sir")
            webbrowser.open('https://twitter.com/')
            Speak("Ok,sir")
            
        elif 'classroom' in query:
            Speak("Ok,sir")
            webbrowser.open('https://classroom.google.com/')
            Speak("Done,sir")
            
            
        # elif 'vscode' in query:
        #     Speak("Ok,sir")
        #     os.startfile('C:\Users\subha\AppData\Local\Programs\Microsoft VS Code\Code.exe')
                
  
        elif 'wikipedia' in query:
            Speak("Searching wikipedia....")
            query = query.replace("valiant","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According to wikipedia : {wiki} ")
            
            
        elif 'screenshot' in query:
                Speak("Ok,sir")
                ss = pyautogui.screenshot()
                ss.save('ss.png')
                Speak("Done,sir")
                
       
            
            
            
  
  
wish()            
Task()         