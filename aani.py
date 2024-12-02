import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
from email.mime.text import MIMEText
import wikipedia
import webbrowser
import os
import random as rand
import smtplib #For emails
engine = pyttsx3.init('sapi5') #API for speech to wikipedia
voices = engine.getProperty('voices')
#print(voices) 
engine.setProperty('voice',voices[1].id)
#print(voices[1].id)  --> TTS_MS_EN-US_ZIRA_11.0 (female)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        print("Good Morning!!")
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!!")
        speak("Good Afternoon!!")
    else:
        print("Good Evening!!")
        speak("Good Evening!!")
    print("Hello! I am Aani. Please tell me how can I help you?")
    speak("Hello! I am Aani. Please tell me how can I help you?")

def takeCommand():
    #It takes microphone input from user and returns it in string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1 #To increase gap between user and computer
        audio = r.listen(source) 
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    msg = MIMEText(content)
    msg['From'] = 'aarathisree15@gmail.com'
    msg['To'] = to
    msg['Subject'] = 'Message'
    # Establish a secure connection using SMTP_SSL for port 465
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('aarathisree15@gmail.com', 'retm vizj seqs etlc')     
    # Send the email
    server.sendmail('aarathisree15@gmail.com', to, msg.as_string())
    server.quit()

if __name__ == "__main__":
    wishMe()
    #Logic for executing tasks:
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'leetcode' in query:
            webbrowser.open('leetcode.com')
        elif 'github' in query:
            webbrowser.open('github.com')
        elif 'hackerrank' in query:
            webbrowser.open('hackerrank.com')
        elif 'music' in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[rand.randint(0,len(songs)-1)])) #Starts playing ta random song
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
        elif 'code' in query:
            codePath = r"C:\Users\AARATHISREE\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("What should I say in the email?")
                content = takeCommand()
                to = input("Enter mail id to send message:")
                speak(f"Sending Message to .. {to}")
                #to = "aarathisree15@gmail.com"
                sendEmail(to,content)
                speak("Email Sent !!")
            except Exception as e:
                #print(e)
                speak("Sorry couldn't send the email.")
        elif 'close' or 'quit' in query:
            speak("Quitting.... Thank you!!")
            break