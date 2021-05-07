import pyttsx3
import time
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser as wb
import os
import warnings
import random
import requests
from gtts import gTTS
import calculator
from calculator.simple import SimpleCalculator
from YMusic import *




engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wakecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(".")
        audio = r.listen(source, phrase_time_limit = 3)

    try:
        print("..")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        
        
    except sr.UnknownValueError:
        return "none"
    return query   
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source, phrase_time_limit = 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        
        
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
        return "none"
    return query   
    
def time1():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak("the current time is")
    print(Time)
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print("the current date is")
    speak("the current date is")
    print(date)
    print(month)
    print(year)

    speak(date)
    speak(month)
    speak(year)


def wishme(i):

    if (i==0):    
       
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour<12:
            print("Good morning sir!")
            speak("Good morning sir")
        elif hour >= 12 and hour<18:
            print("Good afternoon sir!")
            speak("Good afternoon sir")
        elif hour >= 18 and hour<24:
            print("Good evening sir!")
            speak("Good evening sir")
        else :
            print("Hello sir!")
            speak("Hello sir")
        print("Jarvis at your service. Please tell me how can i help you?")
        speak("Jarvis at your service. Please tell me how can i help you?")
    elif (i==1):
        print("Yes!")
        speak("Yes")



def open_application(query): 
  
    if "chrome" in query:
        print("Opening Google Chrome")
        speak("Opening Google Chrome") 
        os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        
  
    elif "firefox" in query or "mozilla" in query: 
        print("Opening Mozilla Firefox") 
        speak("Opening Mozilla Firefox")
        os.startfile(r'C:\Program Files\Mozilla Firefox\\firefox.exe') 
        
  
    elif "microsoft word" in query: 
        print("Opening Microsoft Word")
        speak("Opening Microsoft Word") 
        os.startfile(r'C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE') 
        
  
    elif "microsoft excel" in query: 
        print("Opening Microsoft Excel")
        speak("Opening Microsoft Excel") 
        os.startfile(r'C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE') 
        
  
    else:
        speak("Application is not available , sir")
        speak("Application is not available , sir") 
    return    

def search_on(query):
    if 'google' in query:
        print("what should i search")
        speak("what should i search")
        chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        search = takecommand().lower()
        wb.get(chromepath).open_new_tab('https://www.google.com/search?q='+search)
    elif 'youtube' in query:
        print("what should i search")
        speak("what should i search")
        chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        search = takecommand().lower()
        wb.get(chromepath).open_new_tab('https://www.youtube.com/results?search_query='+search)


def NewsFromGoogle_Ind(): 
    main_url = " http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=4dbc17e007ab436fb66416009dfb59a8"

    open_page = requests.get(main_url).json() 
    article = open_page["articles"] 
    results = []   
    for ar in article: 
        results.append(ar["title"]) 

    for i in range(len(results)):        
        print(i + 1, results[i]) 
        speak(results[i])

def weather(query):
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    query = query.replace("what ","")
    query = query.replace("what's ","")
    query = query.replace("is ","")
    query = query.replace("the ","")
    query = query.replace("temperature ","")
    query = query.replace("in ","")
    query = query.replace("jarvis ","")
    query = query.replace("weather ","")
    print (query)
            
    city_name=query
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        print(" Temperature in " + query + " is " +
        str(round(current_temperature-273,2)) +" degree celcius" +
        "\n humidity is " +
        str(current_humidiy) +"percent")
        speak(" Temperature in " + query + " is " +
        str(round(current_temperature-273,2)) +" degree celcius" +
        "\n humidity is " +
        str(current_humidiy) + "percent")
                
    else:
        speak("no matching results, please speak again")

def simple_calculator(query):
    c=SimpleCalculator()
    query = query.replace("calculate ","")
    query = query.replace("claculator ","")
    query = query.replace("plus","+")
    query = query.replace("x","*")
    query = query.replace("multiply","*")
    query = query.replace("multiply by","*")
    query = query.replace("into","*")
    query = query.replace("divided by","/")
    query = query.replace("divide by","/")
    print(query)
    c.run(query)
    print (c.lcd)
    speak(c.lcd)


def main(i):
    
    wishme(i)
    i=1
    
    while True:
        query = takecommand().lower()
        
        if 'time' in query:
            time1()
        elif 'date' in query:
            date()
        elif 'stop' in query:
            speak("bye, sir")
            print("Bye, Sir")
            break
        elif 'who created' in query or 'who create' in query:
            speak("I was created as a project by 4 creaters")
            print("I was created as a project by 4 creaters")
            break
        elif 'wikipedia' in query:
            speak("searching...")
            print("searching...")
            query = query.replace("wikipedia","")
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace("about","")
            query = query.replace("jarvis","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'open in chrome' in query:
            speak("Which website to open sir?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            print('Opening '+search+ '.com')
        elif 'search on' in query:
            search_on(query)
        elif 'open' in query: 
            open_application(query)
        elif 'roll a dice' in query: 
            no=random.randint(1, 6)
            print(no)
            speak("The number is" + str(no))
            
        elif 'wait' in query:
            time.sleep(10)
            speak('New command sir')
        elif "weather" in query or "temperature" in query:
            weather(query)
        elif 'news' in query or 'headlines' in query:
            NewsFromGoogle_Ind()
        elif 'calculate' in query:
            simple_calculator(query)
        
        elif 'play music' in query or 'play random music' in query or 'play song' in query:
            query = query.replace("play ","")
            query = query.replace(" play ","")
            query = query.replace(" music ","")
            query = query.replace("music ","")
            query = query.replace(" song ","")
            print(query)
            try:
                x=YoutubeMusic()
            except common.exceptions.WebDriverException:
                #! if you have some problmes with web driver.
                print("Error while using Chrome Driver (Possible Causes ) : ");
                print("1. Using Old Chrome Driver, Please Get Latest Version.")
                print("2. Incorrect Path of Chrome Driver Provided, Please Correct It.")
                input();
                exit();
            while True:
                if(x.FirstTime):
                    x.HelpMenu()
                
                
                if (x.firsttmch):
                    contentName = query                    
                

                if(len(contentName) == 0):
                    continue
                
                else:
                    try:
                        x.NavigateYoutube(contentName)
                        x.ListVideos()
                        
                       
                        contentchoice = 1                        
                                                                   
                        if(contentchoice == 0):
                            #!If no input is provided regarding music it will take 1st music out of list.
                            x.PlayVideo(1)
                        elif(contentchoice == 9):
                            #!It will load previous page.
                            x.NavigateYoutube(contentName)
                        else:
                            x.PlayVideo(contentchoice)
                            while True:
                                query = wakecommand()
                                print (query)
                                if("stop" in query  or "STOP" in query ):
                                    x.Close()
                                elif("help" in query  or "HELP" in query  or "=?" in query ):
                                    x.HelpMenu()
                                elif("refresh" in query  or "query" in query ):
                                    x.RefreshPage()
                                elif("Restart" in query or  "restart" in query ):
                                    x.RestartVideo()
                                elif("play" in query  or "PLAY" in query ):
                                    x.Play()
                                elif("pause" in query  or "PAUSE" in query ):
                                    x.Pause()
                                elif("forward" in query or "FORWARD" in query):
                                    if(":" not in query):
                                        x.MoveForward()
                                    else:
                                        Ftime = query.split(":")[1]
                                        if(len(Ftime) == 0):
                                            x.MoveForward()
                                        else:
                                            x.IncreaseTime = Ftime
                                            x.MoveForward()
                                elif("backward" in query or "backward" in query):
                                    if(":" not in query):
                                        x.MoveBackwards()
                                    else:
                                        Ftime = query.split(":")[1]
                                        if(len(Ftime) == 0):
                                            x.MoveBackwards()
                                        else:
                                            x.DecreaseTime = Ftime
                                            x.MoveBackwards()

                                            break

                    
                    except common.exceptions.ElementClickInterceptedException:
                        print("Unknown Error: Please Try Again.")
                        
                    except ValueError:
                        x.NavigateYoutube(contentName)
                        x.ListVideos()
                       

            
        else :
            break 

    return i    
