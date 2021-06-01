# imported modules that are required
import speech_recognition as sr
from playsound import playsound
import pyaudio
import pyttsx3
import platform
import cpuinfo
import webbrowser
import sys
import time
import smtplib
from email.message import EmailMessage

print("setting all things ready....")
x=pyttsx3.init()
voices=x.getProperty('voices')
x.setProperty('rate',120)
x.setProperty('voice', voices[1].id)
x.runAndWait()
        
         
x.say("good morning sir what can i do for you")
x.runAndWait()


# speach recognising system
def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("lisning.....")
        playsound('start.wav')
        r.pause_threshold=0.6
        audio=r.listen(source)
        print("recognising....")
        playsound('stop.wav')
        
    try:
         

        ask=r.recognize_google(audio,language='en-us')
        print(f"you said:{ask}")

        # data
        text=()
        if ask == ("what is your name"):
            text=("my name is moto i hoped you would be knowing.")
        elif ask ==("hello moto"):
            text=("hello sir what can i do for you")
        elif ask==("bye") or ask==("stop") or ask==("close") :
            text=("bye sir, have a nice day")
            sys.exit()
        elif ask==("processor information"):
            print(platform.processor())
            text=(platform.processor())
        elif ask==("cpu information"):
            print(cpuinfo.get_cpu_info())
            text=(cpuinfo.get_cpu_info())
        elif ask==("open web browser"):
            webbrowser.open()
            text=("launching web browser. just a minute")
        elif ask==("cpu info"):
            print(cpuinfo.get_cpu_info())
            text=(cpuinfo.get_cpu_info())
        elif ask==("processor info"):
            print(platform.processor())
            text=(platform.processor()) 
        elif ask==("open google" )or ask==("open Google"):
            webbrowser.open('https://google.com')
        elif ask== ("open youtube") or ask== ("open YouTube"):
            webbrowser.open("https://youtube.com")
        elif ask== ("open whatsapp") or ask== ("open WhatsApp"):
            webbrowser.open("https://web.whatsapp.com/")
        elif ask== ("please provide me a minute") or ask==("sleep") or ask==("keep quite"):
            print("going to sleep for 2 minutes")
            time.sleep(10)
            text=("sir now can i help you?")
        elif ask== ("thank you so much"):
            print("welcome")
            text=("welcome")
        elif ask == ("tell me the time"):
            print(time.asctime(time.localtime(time.time())))
            text=(time.asctime(time.localtime(time.time())))
        #email sending.....
        elif ask==("send email"):
            def get_info():
                try:
                    with sr.Microphone() as source:
                        print('listening...')
                        voice = r.listen(source)
                        info = r.recognize_google(voice)
                        print(info)
                        return info.lower()
                except:
                    pass
            def send_email(receiver, subject, message):
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                # Make sure to give app access in your Google account
                server.login('email id', 'password')
                email = EmailMessage()
                email['From'] = 'email id'
                email['Subject'] = (subject)
                email.set_content(message)
                server.send_message(email)


            def get_email_info():
                name = input("to whome do you want to send e mail:=>")
                print("tell me your subject")
                subject = get_info()
                print("please tell your message")
                message = get_info()
                send_email(name, subject, message)
                print ("your email is sent")
            get_email_info()
        
        else :
             webbrowser.open("https://www.google.com/search?q="+ask)
             text=("searching on the web. please provide me a minute")
             
             

        # speaking system
        x=pyttsx3.init()
        voices=x.getProperty('voices')
        x.setProperty('rate',120)
        x.setProperty('voice', voices[1].id)
        x.runAndWait()


        x.say(text)
        x.runAndWait()


 
    except Exception:
        x=pyttsx3.init()
        voices=x.getProperty('voices')
        x.setProperty('rate',120)
        x.setProperty('voice', voices[1].id)
        x.runAndWait()
    
        
        x.say("sorry unable to recognise say that again...")
        x.runAndWait()

        print("sorry! unable to recognise, say that again...")
        return""
    return 
 
# rerun
while True:
    command()

command()
