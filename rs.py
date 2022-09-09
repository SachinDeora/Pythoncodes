import pyttsx3
import serial
#import times
#import datetime
import pyautogui
#import pyaudio
#import re
import speech_recognition as sr

ArduinoSerial = serial.Serial(port='com5', baudrate=9600)

while 1:
    incoming = str(ArduinoSerial.readline())
    print(incoming)

    if 'Rewind' in incoming:
        print("Running")
        engine = pyttsx3.init()
        engine.say("Welcome to Poddar International College")
        engine.runAndWait()

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-uk')
            print(f"User said: {query}\n")

        except Exception as e:

            speak("Say that again please...")
            # return "None"
            # return query

            if __name__ == "__main__":
                wishMe()
                while True:

                    query = takeCommand().lower()

                    if 'Hello' in query:
                        speak('Hello')

            if 'Forward' in incoming:
                pyautogui.hotkey('ctrl', 'right')

            incoming = ""
