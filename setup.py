import platform
import os
os_name=platform.system()
if os_name=="Windows":
    os.system("pip install pyttsx3")
    os.system("pip install wikipedia")
    os.system("pip install pyautogui")
    os.system("pip install SpeechRecognition")
elif os_name=="Linux" :
    os.system("pip3 install pyttsx3")
    os.system("pip3 install wikipedia")
    os.system("pip3 install pyautogui")
    os.system("pip3 install SpeechRecognition")
else:
    print("This code is not for this OS")
    
