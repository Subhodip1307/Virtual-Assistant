import datetime
import time
import pyttsx3
import speech_recognition as sp
import wikipedia
import webbrowser
import os,pyautogui
def speak(word): #use to pronunce words
    emon=pyttsx3.init("sapi5")
    voices=emon.getProperty("voices")
    emon.setProperty("voice",voices[1].id) #geting female voice
    emon.setProperty("rate",185)
    emon.say(word)
    emon.runAndWait()
def greet_user(): #use to greet the user when user will open it
    hour=datetime.datetime.now().hour
    if hour >=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12  and hour <18:
        speak("Good after noon sir!")
    else:
        speak("Good evening")
    speak("I am Friday a virtual assistance . How may I help you")
def taking_com():
    r=sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        word=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(word,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again.....")
        return "none"
    return query
if __name__ == '__main__':
    greet_user()
    while True:
        query=taking_com().lower()
        if "wikipedia" in query:
            speak("searching for wikipedia")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "bye-bye" in query or "bye Friday" in query or "bye bye" in query :
            speak("Good bye sir ")
            speak("I Love you")
            exit()
        elif "i love you" in query:
            speak("Thanks sir , I love you aslo")
        elif "what is the meaning of" in query:
            pass
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("facebook.com")
        elif "time" in query:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {t}")
        #office iteams
        elif "excel" in query:
            speak("Opening Ms excel")
            excel_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excel_path)
            time.sleep(3)
            pyautogui.press("enter")
        elif "word" in query:
            speak("opening ms word")
            excel_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(excel_path)
            time.sleep(3)
            pyautogui.press("enter")
        elif ("powerpoint" in query) or ("ppt" in query):
            speak("opening Ms power point ")
            excel_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(excel_path)
            time.sleep(3)
            pyautogui.press("enter")
        elif ("writing mode" in query) or "right mode" in query:
            speak("what do you want to write")
            while True:
                wirte=taking_com().lower()
                if wirte != "exit" and wirte != "full stop":
                    speak(wirte)
                    pyautogui.write(wirte)
                    pyautogui.press("space")
                elif wirte=="full stop":
                    pyautogui.write(".")
                    pyautogui.press("space")
                else:
                    speak("quiting the writing mode ")
                    break
        elif ("exit" in query):
            speak("exit")
            pyautogui.keyDown("alt")
            pyautogui.press("f4")
            pyautogui.keyUp("alt")
        elif ("take a screenshot" in query):
            speak("taking a screenshot")
            s=pyautogui.screenshot()
            speak("opening the screenshot")
            s.save("Screenshot.png")
            os.startfile("Screenshot.png")
        elif ("who are you" in query):
            speak("I am emon an virtual assistance developed by Suvodip")
       

