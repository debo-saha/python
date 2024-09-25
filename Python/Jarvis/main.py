import speech_recognition as sr
import pyttsx3
import webbrowser
import music
import requests

key="0a1c3af4f7164a42925ea8fd5ebfb6fe"
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def processComand(c):
    if "open" in c.lower():
        browse=c.lower().split(" ")[1]
        webbrowser.open(f"https://{browse}.com")
    # elif c.lower().startswith("play"):
    #     song=c.lower().split(" ")[1]
    #     link=music.musics[song]
    #     webbrowser.open(link)
    # elif "news" in c.lower():
    #     response=requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=0a1c3af4f7164a42925ea8fd5ebfb6fe")
    #     if response.status_code == 200:
    #         data = response.json()
    #     else:
    #         print(f"Failed to fetch data: {response.status_code}")
    #     articales=data.get("articles",[])
    #     for articale in articales:
    
    #         speak(articale['title'])
    
            
speak("Initializing Jarvis .....")



while True:
    # liistening from microphone
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,phrase_time_limit=1)
            word= r.recognize_google(audio)
        if(word.lower()=="jarvis"):
            speak("Ya")
            with sr.Microphone() as source:
                print("Jarvis activated...")
                new_audio = r.listen(source)
                newcomand= r.recognize_google(new_audio)
                print(newcomand)
                processComand(newcomand)
        else:
            print(word)
    except Exception as e:
        print("Error; {0}".format(e))
