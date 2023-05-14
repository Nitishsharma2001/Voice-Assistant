import playsound as playsound
import pyttsx3
import time
import speech_recognition as sr
import webbrowser
import datetime
from datetime import date
import pywhatkit as kt
from tkinter import scrolledtext
import requests
import pyautogui
import wikipedia
import os
import tkinter as tk
from tkinter import *
import pyjokes
import subprocess

# initialisation
engine = pyttsx3.init()
# Speak function
named_tuple = time.localtime()
time_string = time.strftime("%H", named_tuple)


def speak(audio):
    engine.setProperty("rate", 150)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    if int(time_string) > 12 and int(time_string) < 16:
         engine.say("Good Afternoon sir.")
    elif int(time_string) < 12 and int(time_string) > 6:
         engine.say("Good Morning sir.")
    elif int(time_string) > 4 and int(time_string) < 20:
         engine.say("Good Evening sir.")
    elif int(time_string) > 8 and int(time_string) < 11:
         speak("Good Night sir.")
    speak("My name is tom. how i can help you sir")
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        playsound.playsound("C:\\Users\\nitis\\PycharmProjects\\main.py\\ring.mp3")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        # print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        speak(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data
def working(a):
    if a=="open google":
        speak("What u want to search sir?")
        query=takeCommand().lower()
        kt.search(query)
    elif a=="open youtube":
        speak("What to search sir")
    # str=takeCommand().lower()
        webbrowser.open('www.youtube.com')
    elif a=="time":
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
    elif a=="date":
         today=date.today()
         speak(f"Sir, the date is {today}")
    elif a=="search":
         speak("how i can help you sir.")
         q=takeCommand().lower()
         kt.search(q)
    elif a=="text to speech":
         def speechdata():
             data = textpad.get('1.0', END + '-1c')
             speak(data)
         t1 = tk.Tk()
         t1.geometry('600x500+300+100')
         textpad = scrolledtext.ScrolledText(t1, width=800, height=580, undo=True)
         t1.title('Text to speech (Enter the text here)')
         t1.configure(bg='white')
         t1.resizable(width=True, height=True)
         t1.iconbitmap("logo.ico")
         b1 = Button(t1,text="Speech", height=1, width=10, command=speechdata)
         b1.pack()
         textpad.pack()
         mainloop()
    elif a=="speech to text":
         a = takeCommand().lower()
         sample = open("C:\\Users\\nitis\\OneDrive\\Documents\\sample.txt", 'w')
         sample.write(a)
         sample.close()
    elif a=='location':
         speak(get_location())
    elif a=="take screenshot" or a=="screenshot":
         im = pyautogui.screenshot()
         im.save("SS2.jpg")
    elif a=="command prompt" or a=="cmd":
         os.startfile("C:\\WINDOWS\\system32\\cmd.exe")
    elif a=="search for music file":
         speak("what is yours file name sir?")
         file_name=takeCommand()
         file_name.lower()
         f=os.path.exists(f"E:\\music\\{file_name}.mp3")
         if not f:
            speak("Not found sir!")
         else:
            speak("Found sir!. you want to open it or not?")
            g=takeCommand()
            if g == 'not' or 'no':
               speak("okk sir!")
            elif g == 'yes'or 'open':
                 # address=f"E:\\music\\{file_name}.mp3
                 os.startfile(f"E:\\music\\{file_name}.mp3")
    elif a=='wikipedia' :
        speak("What you want to search on wikipedia sir ")
        c=takeCommand()
        speak('Searching Wikipedia...')
        c = c.replace("wikipedia", "")
        results = wikipedia.summary(c, sentences=2)
        speak("According to Wikipedia")
        speak(results)

    # w="who is"
    # w1="what is"
    elif a.startswith("who is")  or a.startswith("what is"):
        # speak("What you want to search on wikipedia sir ")
        # speak('Searching Wikipedia...')
        a = a.replace("wikipedia", "")
        results = wikipedia.summary(a, sentences=3)
        # speak("According to Wikipedia")
        speak(results)
    elif 'about' in a:
        speak("I was developed by Nitish Sharma , 10% mohit bajaj and 20% jatin arora ")
    elif 'joke' in a:
        speak(pyjokes.get_joke())

    elif 'shutdown' in a:
        speak("system is shutting down sir!")
        subprocess.call('shutdown / p /f')

    else:
        speak("Found this on google!")
        kt.search(a)
def temp_text(e):
   e1.delete(0,"end")
def mic():
   # wishme()
   a=takeCommand().lower()
   working(a)
def get_text(event):
    a=e1.get()
    working(a)
    e1.delete(0, END)
def feedback():
    speak("ok give your feedbacks sir it realy helps me alot to improve mysekf")
    a=takeCommand()
    f=open("C:\\Users\\nitis\\OneDrive\\Desktop\\feedbacks.txt",'a')
    f.write(a)
    speak("Feedback done sir")
# if _name_ == '_main_':
     #Creating window
root=tk.Tk()
root.title("Tom")
root.geometry("500x225")
root.configure(background="#030303")
menubar = Menu(root)
# root.iconbitmap("logo.ico")
# Declare file and edit for showing in menubar
file = Menu(menubar, tearoff=False)
# Add commands in file
file.add_command(label="feedback",command=feedback)
file.add_command(label="about")
file.add_command(label="exit",command=exit)
def exit():
    root.destroy()
# Display the file and edit declared in previous step
menubar.add_cascade(label="Help", menu=file)
# Displaying of menubar in the app
e1=Entry(root,width=40,bg="#1A1A1A",fg="white",font=('Arial 12'),bd=0)
e1.insert(0,"  Ask any querry!")
e1.place(x=10,y=165)
e1.bind("<FocusIn>", temp_text)
root.bind('<Return>',get_text)
root.config(menu=menubar)
icon=PhotoImage(file="mic.png")
b1=Button(root,image=icon,width=40,height=40,relief=FLAT,bg="#030303",activebackground="#030303",command=mic)
b1.place(x=450,y=150)
logo=PhotoImage(file="logo.png")
frame = Frame(root, width=10, height=10)
frame.pack()
label = Label(frame, image = logo,bg="#030303")
label.pack()
l6=Label(root,text="Hi how i can help you?",height=1,width=20,font=('Arial 12'),bg="#030303",fg="#3B3B3B")
l6.pack()
root.mainloop()