import pyttsx3 # audio library
import datetime
import speech_recognition as sr #command taking library
import wikipedia
import smtplib
#import sys 
#sys.stderr.fileno()


engine = pyttsx3.init()


def speak(audio): # speak function
    engine.say(audio)
    engine.runAndWait()



def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir")
    time()
    date()
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    elif hour>=18 and hour<24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Carv is at your service.Please tell me how can i help you?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return "None"
    return query

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abzc@gmail.com','123')
    server.sendmail('abzc@gmail.com',to,content)
    server.close()
    

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if "time" in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Seraching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to='xyz@gmail.com'
                #sendEmail(to,content)
                speak(content)
            except Exception as e:
                print(e)
                speak("unable to send email")
        elif 'offline' in query:
            quit()