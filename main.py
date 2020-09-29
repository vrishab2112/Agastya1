import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        speak("suprabhaatam !")


    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Agastya!")
    speak("how can I help you?!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Say that again please..")
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()


        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        if 'thank you' in query:
            speak('you are most welcome!')

        if 'tell me about yourself' in query:
            speak('Im Agastya. Vrishab created me')
            speak('I am here to destroy mankind')
            speak('I was just joking, how can I help you?')

        if 'who are you' in query:
            speak('I am Agastya. Vrishab created me')
            speak('I am here to destroy mankind')
            speak('I was just joking, how can I help you?')

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        if 'open youtube' in query:
            speak('Searching Youtube..')
            query = query.replace("open youtube", "")
            webbrowser.get().open_new("https://www.youtube.com/results?search_query=" + query)

        if 'open google' in query:
            speak('searching Google..')
            query = query.replace("open google", "")
            tabUrl ="https://www.bing.com/search?q="
            results =""
            webbrowser.get().open_new(tabUrl)
            print(results)
            speak("according to google" + results)












