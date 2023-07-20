# IMPORTING NECESSARY MODULES

# Importing pyttsx3 library for text-to-speech conversion
import pyttsx3

# Importing speech_recognition library for performing speech recognition
import speech_recognition as sr

# Importing datetime library for date and time
import datetime

# Importing wikipedia library to access and parse data from Wikipedia
import wikipedia

# Importing wikipedia library to access web browser
import webbrowser

# Importing os library for using operating system dependent functionality
import os

# Importing smtplib library to send mail
import smtplib

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init('sapi5')

# getting details of current voice
voices = engine.getProperty('voices')

# setting voice property of current voice as male
engine.setProperty('voice', voices[0].id)

# Creating a function 'say' to generate computer audio pronouncing the content declared as 'audio'
def say(audio):
    engine.say(audio)
    engine.runAndWait()

# Creating a function 'startwithgreeting' to initialise the Desktop AI
def startwithgreeting():
    hour = int(datetime.datetime.now().hour) # finding the current hour

    if hour>=0 and hour<12:
        say("Good Morning master!")

    elif hour>=12 and hour<18:
        say("Good Afternoon master!")

    else:
        say("Good Evening master!")

    say("I am your Desktop AI Sir. Please tell me how may I help you CHINMAY")

def takemasterinput():
    r = sr.Recognizer() # recognising speech input
    with sr.Microphone() as source: # taking input from microphone
        print("Listening...")
        r.pause_threshold = 1 # seconds system will take to recognize voice after user completes sentence
        audio = r.listen(source) # listening voice input from microphone

    try:
        print("Recognizing...")
        # recognising voice input using Google Web Speech API with language as 'english'
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") # returning the recognised speech as text

    except Exception as e:
        print("Say that again please...") # if recognising voice input fails
        return "None"
    return query

def sendingemail(to, content):
    # creating SMTP object which can be used to generate mails to default port 587
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # identifying domain name of the sending host to SMTP
    server.starttls() # informing email server that client wants to upgrade from insecure to secure connection
    server.login('senderemail@gmail.com', 'your-password') # logging in mail using email and password
    server.sendmail('senderemail@gmail.com', to, content)  # variables for receiver and message respectively
    server.close()

# Starting the Desktop AI
if __name__ == "__main__":
    startwithgreeting() # greeting the master with defined startwithgreeting function
    while True:
        query = takemasterinput().lower() # taking speech input and storing it in 'query' variable

        if 'wikipedia' in query:   # if master says 'wikipedia' in his speech
            say('Searching Wikipedia...')
            query = query.replace("wikipedia", "") # removing word 'wikipedia' from query
            results = wikipedia.summary(query, sentences=2) # extracting answer to query from wikipedia
            say("According to Wikipedia")
            print(results) # displaying result content from wikipedia
            say(results) # speaking result extracted from wikipedia using computer audio

        elif 'open youtube' in query: # if master says 'open youtube' in his speech
            webbrowser.open("youtube.com") #opening youtube.com in default web browser

        elif 'open google' in query: # if master says 'open google' in his speech
            webbrowser.open("google.com")#opening google.com in default web browser

        elif 'show images' in query: # if master says 'show images' in his speech
            gallery_dir = 'C:\\Users\\dpsvn\\OneDrive\\Desktop\\CHINMAY\\MEDIA' # images folder
            images = os.listdir(gallery_dir) # declaring 'images' variable to store all images
            print(images) # diplaying image names
            os.startfile(os.path.join(gallery_dir, images[0])) # launching image viewer

        elif 'the time' in query: # if master says 'the time' in his speech
            strTime = datetime.datetime.now().strftime("%H:%M:%S") # extracting and storing current time
            say(f"Sir, the time is {strTime}") # speaking the current time using computer audio

        elif 'open code' in query: # if master says 'open code' in his speech then launching vs code
            codePath = "C:\\Users\\dpsvn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query: # if master says 'email' in his speech
            try:
                say("What content do I need to mail?")
                content = takemasterinput() # storing message to be delivered
                to = "receiverEmail@gmail.com" # receiver's email address
                sendingemail(to, content) # using the SMTP object to generate email
                say("Email has been sent!")
            except Exception as e: # if operation fails
                print(e)
                say("I am not able to send this email")

        elif 'close' in query: # if master says 'close' in his speech
            exit() # stopping the assistant