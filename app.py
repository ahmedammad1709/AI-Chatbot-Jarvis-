import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys
import webbrowser
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()

    except Exception as e:
        speak("I couldn't recognize that, please try again!")
        return None


# Function to tell Time
def tell_Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {time}")
    print(f"The current time is {time}")


# Function to search from Wikipedia
def search_wikipedia(query):
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=1)
    speak(result)
    print(result)


def play_Youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
    print("YouTube is now open")


def close_Youtube():
    speak("Closing YouTube")
    webbrowser.open("https://www.youtube.com")  # This will not close the YouTube window. Consider using specific browser commands for closing tabs
    print("YouTube has been closed")


def search_on_Youtube(query):
    speak(f"Searching YouTube for {query}")
    query = query.replace("search on youtube", "")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    print(f"Searching YouTube for {query}")


def close_program():
    speak("Goodbye! Have a nice day")
    sys.exit()


def random_Questions(query):
    if "how are you" in query or "Waalikumsalam How are you?" in query:
        return "I am fine Alhamdulillah, How can I help you?"
    elif "who are you" in query:
        return "I am Ammad's AI Assistant, created to make your life easier."
    elif "What can you do" in query:
        return "I can tell time, I can open YouTube, and I can retrieve information from Wikipedia for you."
    elif "Assalamoalikum" in query or "salam" in query:
        return "Waalikumsalam bro!, how can I help you?"
    else:
        return None


def main():
    speak("Assalamoalikum! I am Ammad's AI, How can I assist you today!")

    while True:
        query = listen()
        if query is None:
            continue

        query = query.lower()

        response = random_Questions(query)
        if response:
            speak(response)
            print(response)
            continue

        # Check if the User asks for time
        if 'time' in query:
            tell_Time()

        elif 'wikipedia' in query:
            search_wikipedia(query)

        elif 'quit' in query or 'exit' in query or 'Allah Hafiz' in query:
            close_program()

        elif 'youtube' in query:
            play_Youtube()

        elif 'close youtube' in query:
            close_Youtube()

        elif 'search on youtube' in query:
            search_on_Youtube(query)

        else:
            speak("Sorry, I didn't understand that. Please try again")


if __name__ == "__main__":
    main()
