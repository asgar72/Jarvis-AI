import pyttsx3  #pip install pyttsx3
import time
import datetime
from datetime import date
import speech_recognition as sr  #pip install SpeechRecognition
import wikipedia  #pip install wikipedia
import webbrowser
import os
import random 
import cv2   #camera
import ctypes  #lock screen
import subprocess
from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontend import Ui_MainWindow


engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! Sir")
        speak("Good Morning! Sir")         
    elif hour>=12 and hour<18:
        print("Good afternoon Sir")
        speak("Good afternoon Sir")       
    else:
        print("Good evening Sir")
        speak("Good evening Sir")
        
    print("I am Jarvis. The AI Assistent of Asgar Please tell me how may I help you ?")
    speak("I am Jarvis  !The A.I. assistent of ,   Asgar , Please tell me , how may I help you ? ")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()
        speak("please say wakeup to continue")
        while True:
            self.query = self.takecammand()
            if "wake up"in self.query or "are you there"in self.query or "hello" in self.query:
                self.TaskExecution()
    
    def takecammand(self):
        #it takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")  
        except Exception as e:
            # print("Say that again please...")
            return "None"   
        return self.query

    def TaskExecution(self):
        clear = lambda: os.system('cls')
        clear()
        wishMe()
        while True:
         
            self.query = self.takecammand().lower()
    
            # Logic for executing  tasks based on self.query
            # All the commands said by user will be 
    
            if  'Good night'in self.query :
                if'good night' in self.query:
                    hour =int(datetime.datetime.now().hour)
                    if ((hour>=21 and hour<24)or(hour>=0 and hour<=1)):
                        speak("ok sir , Good night ... I am always with you sir , bye , Take care..")
                    else:
                        speak("No sir.. Dont make me a Fool...  ")
                    

    
            elif(('good morning' in self.query)or('good afternoon'in self.query)or('good evening'in self.query)):
    
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    print("Good Morning! Sir")
                    speak("Good Morning! Sir")         
                elif hour>=12 and hour<18:
                    print("Good afternoon Sir")
                    speak("Good afternoon Sir")       
                else:
                    print("Good evening Sir")
                    speak("Good evening Sir")
    
            elif'hello'in self.query:
                print("Hello Sir , what can i do for you")
                speak("Hello Sir , what can i do for you")
    
            elif'name'in self.query:
                print("I am A.I. based sophia ,i am assistent of Asghar")
                speak("I am A.I. based sophia ,i am assistent of Asghar")

            
            elif(('the time' in self.query)or('time' in self.query)):
                strTime = datetime.datetime.now().strftime("%H:%M:%S")  
                print(f"the time is {strTime}")
                speak(f"the time is {strTime}")
    
            elif(('the date'in self.query)or('date'in self.query)):
                strTime = datetime.datetime.now().strftime("%m/%d/%Y")  
                print(f"Sir the date is {strTime}")
                speak(f"Sir, the date is {strTime}")
    
            elif'wikipedia' in self.query:
                speak('searching wikipedia...')
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query,sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results) 
    
            elif'open youtube' in self.query:
                print("opening Youtube")
                speak("opening Youtube")
                webbrowser.open("http://youtube.com")
    
            elif'open google' in self.query:
                speak("sir ,what should i search on google")
                cm = self.takecammand().lower()
                webbrowser.open(f"{cm}")
    
            elif(('open stackoverflow'in self.query)or('flow'in self.query)):
                speak("Here you go to Stack Over flow.Happy coding")
                webbrowser.open("http://Stackoverflow.com")
                
            elif'open whatsapp' in self.query:
                webbrowser.open("https://web.whatsapp.com")
    

            
            elif'open code' in self.query:
                codePath = "C:\\Users\\Asghar abbas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
    
            elif'command prompt' in self.query or 'open cmd' in self.query:
                speak('openning ,command prompt')
                os.system("start cmd")
    
            elif(('open camera'in self.query)or('camera'in self.query)):
                speak("ok sir opening the camera")
                cap = cv2.VideoCapture(0)
                while True:     
                    ret, img = cap.read()                
                    cv2.imshow('Webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows
    
            elif 'noha' in self.query:
                speak("ok sir play noha")
                noha_dir = 'F:\\Noha\\Shadman'
                noha = os.listdir(noha_dir)
                print(noha)
                random_number = random.randrange(1, 9)
                os.startfile(os.path.join(noha_dir, noha[random_number]))

            elif 'song' in self.query:
                speak("ok sir play noha")
                noha_dir = 'F:\\Noha\\Songs'
                noha = os.listdir(noha_dir)
                print(noha)
                random_number = random.randrange(1, 9)
                os.startfile(os.path.join(noha_dir, noha[random_number]))

            elif'close chrome' in self.query:
                speak('closing chrome...')
                os.system('taskkill /F /IM chrome.exe')
    
            elif'window maximize' in self.query:
                speak('maximize window')
                os.system('"c:\Windows\System32\wbem"')
    
            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
    
            elif "restart" in self.query:
                speak("Hold On a Sec ! Your system is on its way to restart")
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])
    
            elif 'shutdown system' in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
    
            elif'close vlc' in self.query:
                speak('closing vlc..')
                os.system('taskkill /im vlc.exe')

            else:
                print("Do you have any other work")
                speak("Do you have any other work")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/Jarvis AI/7LP81.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/Jarvis AI/T8bahf1.gif")        
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication([])
jarvis = Main()
jarvis.show() 
exit(app.exec_())

