from urllib import response
import speech_recognition as sr
import webbrowser
import pyttsx3
import MUSIC
import requests
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000  # Increase energy threshold
recognizer.dynamic_energy_threshold = True  # Enable dynamic threshold
recognizer.pause_threshold = 0.8  # Reduce pause threshold
engine = pyttsx3.init()
newsapi ="403d25c5377e40b6bc1a2f3bd6b9fdec"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith ("play"):
        song= c.lower().split("")[1]
        link =MUSIC.music[song]
        webbrowser.open(link)

    elif "news" in  c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=403d25c5377e40b6bc1a2f3bd6b9fdec")
        # Check if the request was successful
    if r.status_code == 200:
        data = r.json()
        articles = data.get("articles", [])
    
        print("\nTop Headlines:\n")
    for i, article in enumerate(articles, 1):
        speak(f"{i}. {article['title']}")
    else:
        print("Failed to fetch news:", response.status_code, response.text)

    
    

if __name__=="__main__":
    speak("INITIALIZING BAT...")
    while True:
    #LISTEN FOR THE WAKE WORD "BAT"
    # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
    
        try:
            with sr.Microphone() as source:
                print("LISTENING...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=3, phrase_time_limit=5)

            word=r.recognize_google(audio)
            if "bat" in word.lower():
                speak("CONNECTED")

                with sr.Microphone() as source:
                    speak("bat ACTIVE..")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
              print("Error; {0}".format(e))
              speak("Sorry, I didn't catch that. Please try again.")
