#from calendar import month
#import datetime


import sys
import tkinter
from gpiozero import LED
import cv2
import pause






#from unicodedata import name
from winreg import QueryValue
from numpy import roots
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import pywhatkit
import wikipedia 
import pyjokes
import webbrowser as wb
import os
import time
import subprocess
import pyautogui



import wolframalpha  
import json
import requests
from tkinter import *
from time import sleep
import tkinter as Tk
from ecapture import ecapture as ec
import random
from random import randint 
import serial 
from tkinter import Image, Text, Tk


from tkinter.ttk import Combobox

from tkinter import messagebox, filedialog
import sqlite3



name_assistant='REX'
port='COM6'
baud ='9600'
ser = serial.Serial(port,baud)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)








glad = 'thanks'
det = 'face detection'
userName= 'PATRICK'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voicespeed = 177
engine.setProperty('rate', voicespeed)


  

#def wikipedia_screen(text):
    

  #wikipedia_screen = Toplevel(screen)
  #wikipedia_screen.title(text)
  #wikipedia_screen.iconbitmap('app_icon.ico')

  #message = Message(wikipedia_screen, text= text)
  #message.pack()
  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
  Time= datetime.datetime.now().strftime("%I:%M:%p")
  speak(Time)

def date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()

    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 
    

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        

    subprocess.Popen(["notepad.exe", file_name])
def webcam():
    ret, frame = cap.read()
    cv2.imshow("worldtec_CAM",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit()


def wishme():
    speak("hi !")
    
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning sir!")
        speak("worltec at your service. please tell me how can i help you?")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
        speak("worltec at your service. please tell me how can i help you?")
    elif hour>=18 and hour<24:
        speak("Good evening sir")
        speak("worltec at your service. please tell me how can i help you?")
   
    else:
        speak("Good night sir. sleep well but don't forget to pray")
        
if not ser.isOpen():
    speak("Establishing the connection with the Arduino board! Please, wait a moment!")
    pause.seconds(5)
    speak("the connection has been established!")
    speak("Hello! my name is Worldtec!")
    
    
    ser.open()
print('COM6 is open', ser.isOpen() )
       



def takecommand():
    r = sr.Recognizer()
    try:

        with sr.Microphone()as source:
            #speak ('listening')
            print("Listening.......\/")
            r.pause_threshold = 1
            audio= r.listen(source)
            print("Recongnizition...")
            query = r.recognize_google(audio, language='lug')
            query = query.lower()
            print(query)
    except Exception as e:
            print(e)
            return "none"
    return query



speak("Noted with thnaks")
def play_songs():
   
    music_dir = r"D:\DOCUMENTS\New folder\USB Drive"
    
    speak('which song should i play for you sir?')
    musics = os.listdir(music_dir)
    
    os.startfile(os.path.join(music_dir,musics[0]))
    
if __name__=='__main__':

    while True:
        query = takecommand().lower()
        print(query)

        if "hello" in query or "hi" in query:
            wishme()
        if 'play music'in query:
            play_songs()
        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif "show me the screenshot" in query:
             try:
                img = Image.open(r'C:\Users\BETTY\Desktop\shots')
                img.show(img)
                speak("Here it is sir")
                time.sleep(2)

             except IOError:
                speak("Sorry sir, I am unable to display the screenshot")
        elif 'wait' in query:
            speak("for how many minutes you want me to stop listening?")
            ans = int(takecommand())
            speak("you told me to stop listening to your commands for:" + str(ans)+"minutes")
            pause.minutes(ans)
            speak("I'm back" + userName)
        elif 'miss' in query or 'miss you' in query:
            speak("I missed you too " + userName + "!"+"you've been such a cool guy!")
            speak("Now! tell me how can I help you!")
        elif 'plan' in query:
            speak("you look so excited " + userName)
            speak("that's really great!")


        elif 'lamp on' in query or ' turn on light' in query or 'lights on' in query or 'tekako' in query or 'bulb on' in query or 'turn on lights' in query: 
            
            ser.write(b'L')
            speak('turning on the lamp!')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")

            
        elif 'room light' in query or 'room lights on' in query:
            
            ser.write(b'M')
            speak ('turning on room lights sir')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif 'room light off' in query or 'room off' in query:
            
            ser.write(b'm')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif 'security lights off' in query or 'security off' in query or 'security' in query or 'security light off' in query:
            
            ser.write(b'p')
            speak ('turning off security lights sir')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!") 
        elif 'security lights on' in query or 'security on' in query or 'security light on' in query:
            
            ser.write(b'P')
            speak ('turning on security lights sir')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")   
        elif 'off the lamp' in query or 'lights off' in query or 'turn off light'in query or 'switch off light' in query or 'jako' in query or 'lamp off' in query:
            speak("turning off the lamp!")
            ser.write(b'l')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif 'doorON' in query or 'open door' in query:
            ser.write(b'D')
            speak("alright" + userName + "the door is opened!")
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")

        elif 'dooroff' in query or 'close door' in query or 'lock door' in query or 'lock' in query:
            ser.write(b'd')
            speak("okay" + userName + 'closing the door!')
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif 'air conditioner' in query or 'turn on ac' in query or 'ac on' in query or 'on air'in query:
            ser.write(b'C')
            speak("switching on the air conditioner!")
            query = takecommand()
            if glad in query:
                speak("You're welcome" + userName+ "!")
        elif'off air ' in query or 'ac off' in query or 'off air conditioner'in query:
                ser.write(b'c')
                speak("Switching off the Air conditioner" + userName)
                query = takecommand()
                if glad in query:
                    speak("You're welcome" + userName+ "!")

        elif 'offline' in query:
            speak("ok" +userName +  "see you next time")
            quit()
        elif 'make a note' in query:
            query = query.replace("make a note", "")
            note(query)
        elif 'note' in query:
            speak("what do you want me to remember?")
            data = takecommand()
            speak("you told me to remember " + data)
            note = open("data.txt", "w")
            note.write(data)
            note.close()
        elif 'locate' in query:
            query = query.replace('locate','')
            location = query
            speak(userName + "you asked me to locate" + location)
            wb.open_new_tab("https://www.google.com/maps/" + location)
        elif 'play on youtube'in query:
            song = query.replace('play on youtube','')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
        elif det in query:
            speak("Starting face detection " + userName)
            webcam()
        elif 'temp' in query or 'temperature' in query:
            if ser.in_waiting > 0:
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                datasplit = cookedserial.split(',')
                temperature = datasplit[0].strip('<')
                humidity = datasplit[1].strip('>')
                speak("the sensor is registring a temperature of " + temperature + "degrees Celcius!" + "and a humidity of" + humidity + "percent")
        elif 'open chrome' in query:
            speak('what should i search?')
            chromepath=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            search = takecommand().lower()
            wb.get(chromepath).open(search + ".com")
            chrome=subprocess.Popen(chromepath)
        elif 'content' in query:
            note = open("data.txt", "r")
            speak("Yes" + userName)
            speak("you told me to remember " + note.read())
            speak("Google chrome is opening now")
        elif 'open excel' in query:
            excelpath=r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            excel=subprocess.Popen(excelpath)
            speak("Microsoft office Excel is opening now")
        elif 'powerpoint' in query:
            pointpath=r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            powerpoint=subprocess.Popen(pointpath)
            speak("Microsoft office PowerPoint is opening now")
        elif 'open word' in query:
            wordlocation=r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            word =subprocess.Popen(wordlocation)
            speak("Microsoft office Word is opening now")
        elif 'open publisher' in query:
            pubpath=r"C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE"
            publisher=subprocess.Popen(pubpath)
            speak("Microsoft office publisher is opening now")
        elif "open notepad" in query:
            speak("opening notepad")
            location = r"C:/WINDOWS/system32/notepad.exe"
            notepad = subprocess.Popen(location)
        elif "close publisher" in query:
            speak("closing publisher")
            publisher.terminate()
        elif "close word" in query:
            speak("closing word")    
            word.terminate()
        elif "close excel" in query:
            speak("closing excel")
            excel.terminate()
        elif "close powerpoint" in query:
            speak("closing notepad")
            powerpoint.terminate()
        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()
        elif "task manager" in query:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
        elif "task view" in query:
            pyautogui.hotkey('winleft', 'tab')
        elif "take screenshot" in query:
            pyautogui.hotkey('winleft', 'prtscr')
            img = pyautogui.screenshot()
            img.save(r"C:\Users\BETTY\Desktop\shots\screenshot.png") 
            speak("Done")
        elif "show me the screenshot" in query:
            try:
                img = Image.open(r"C:\Users\BETTY\Desktop\shots\screenshot.png")
                img.show(img)
                speak("Here it is sir")
                time.sleep(2)

            except IOError:
                speak("Sorry sir, I am unable to display the screenshot")    
        elif "setting" in query:
            pyautogui.hotkey('winleft', 'i')
        elif "hidden menu" in query:
            pyautogui.hotkey('winleft', 'x')
        elif "new virtual desktop" in query:
            pyautogui.hotkey('winleft', 'ctrl', 'd')
        elif 'time' in query:
            Time= datetime.datetime.now().strftime("%I:%M:%p")
            print(Time)
            speak('current time is' + Time)

        elif 'good bye' in query or 'ok bye' in query or 'stop' in query:
            speak('Your personal assistant REX is shutting down, Good bye')
            #screen.destroy()
        elif 'wik' in query or 'search'in query or 'wikepedia'in query:
            speak("what do you want me to search?")
            query = takecommand()
            speak("Alright " + userName + "wait a minute!")          

            person = query.replace('wik' or 'search' or 'wikepedia',"")
            try:
                info = wikipedia.summary(person, sentance=3)
                print(info)
                speak(info)
            except:
                speak('page not found')
        elif 'date'in query:
            date()

        elif 'are you single' in query:
            speak (' no! I am in relationship with Jesus and love pancakes.')


        elif 'who are you' in query:
            speak (' I am  worldtec your home voice assistant verion 0.1')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by superinteligent engneer PATRICK and IVAN from Makerere University department of computer and electrical engneering supervised by DR. RONALD")
            print("I was built by superinteligent engneer PATRICK and IVAN from Makerere University department of computer and electrical engneering supervised by DR. RONALD")
        elif ' joke' in query:
            speak(pyjokes.get_joke())
        elif 'what can you do' in query:
            speak(' I am programmed to minor tasks like''opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather In different cities, get top headline news from new vision, daily monitor, open computer applications like word document, pulisher,chrome, zoom, take screenshots, and major tasks like controling devices connected to arduino board such lights, ac, open door final but not the least you can ask me computational or geographical questions too!')

        elif 'ask' in query:
            speak('Iam at your service!,to answer to computational and geographical questions  and what question do you want to ask now')
            question = takecommand()
            app_id="R2K75H-7ELALHR35X "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        
        elif 'online'  in query:
            query = query.replace("online", "")
            wb.open_new_tab(query)
            sleep(5)
        elif 'news' in query:
            news = wb.open_new_tab('https://www.newvision.co.ug/news/1423416/todays-vision-newspaper-headlines')
            speak('Here are some headlines from the new vision,Happy reading')
            sleep(6)

        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0,True,"img.jpg")
            sleep(5)
        elif 'open youtube' in query:
            wb.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            sleep(1)
           

        elif 'open google' in query:
            wb.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            sleep(5)
            
        elif 'open gmail' in query:
            wb.open_new_tab("gmail.com")
            speak("Google Mail open now")
            sleep(5)
        elif "weather" in query:
            api_key="fa615c0452e361addeb1f037c63f953d"
            
            units_format = "&units=metric"

            base_url="https://api.openweathermap.org/data/2.5/weather?"
           
            speak("what is the city name")
            city_name = takecommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url.format(city_name ))
            city_weather_data=response.json()
            if city_weather_data["cod"]!="404":
                main_data = city_weather_data["main"]
                weather_description_data = city_weather_data["weather"][0]
                weather_description = weather_description_data["description"]
                current_temperature = main_data["temp"]
                current_pressure = main_data["pressure"]
                current_humidity = main_data["humidity"]
                wind_data = city_weather_data["wind"]
                wind_speed = wind_data["speed"]

                ''''
                print(" Temperature in kelvin unit = " +str(current_temperature) +"\n humidity (in percentage) = " + str(current_humidity) +"\n description = " +str(weather_description))
                final_response = f"""
                The weather in {city_name} is currently {weather_description} 
                with a temperature of {current_temperature} degree celcius, 
                atmospheric pressure of {current_pressure} hectoPascals, 
                humidity of {current_humidity} percent 
                and wind speed reaching {wind_speed} kilometers per hour"""

                speak (final_response)
                '''
                speak(" Temperature in kelvin unit is " +str(current_temperature) +"\n humidity in percentage is " +str(current_humidity) + "\n description  " +str(weather_description))
                print(" Temperature in kelvin unit = " +str(current_temperature) +"\n humidity (in percentage) = " + str(current_humidity) +"\n description = " +str(weather_description))

            else:
                speak ("Sorry Sir, I couldn't find the city in my database. Please try again")
        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
    
            
        elif "good bye" in query or "ok bye" in query or "stop" in query:
            speak('Your personal assistant ' + name_assistant +' is shutting down, Good bye')
            #screen.destroy()
            break
        else:
            speak('please say it again.')   
    
def change_name():
    name_info = name.get()

    file=open("Assistant_name", "w")

    file.write(name_info)

    file.close()

    settings_screen.destroy()

    screen.destroy()


def change_name_window():
    global settings_screen
    global name


    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("300x300")
    settings_screen.iconbitmap('app_icon.ico')

      
    name = StringVar()

    current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
    current_label.pack()

    enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
    enter_label.pack(pady=10)   
      

    Name_label = Label(settings_screen, text = "Name")
    Name_label.pack(pady=10)
     
    name_entry = Entry(settings_screen, textvariable = name)
    name_entry.pack()


    change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
    change_name_button.pack(pady=10)


def info():
    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')

    creator_label = Label(info_screen,text = "Created by Abhhi Sannayya")
    creator_label.pack()

    Age_label = Label(info_screen, text= " at the age of 12")
    Age_label.pack()

    for_label = Label(info_screen, text = "For Makerspace")
    for_label.pack()

def main_screen():

      global screen
      screen = Tk()
      screen.title(name_assistant)
      screen.geometry("100x250")
      screen.iconbitmap('app_icon.ico')


      name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
      name_label.pack()


      microphone_photo = PhotoImage(file = "assistant_logo.png")
      microphone_button = Button(image=microphone_photo, command = takecommand)
      microphone_button.pack(pady=10)

      settings_photo = PhotoImage(file = "settings.png")
      settings_button = Button(image=settings_photo, command = change_name_window)
      settings_button.pack(pady=10)
       
      info_button = Button(text ="Info", command = info)
      info_button.pack(pady=10)

      screen.mainloop()



    

   


             



       
#while True:
   #run_patrick()





