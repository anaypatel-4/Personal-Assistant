import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def intro():
    talk('Hi I am jemma,what can I do for you today?')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'mark' in command:
                command = command.replace('mark', '')

            print('command>' +command)
            return command
    except:
        print('ERROR LISTENING')
        pass

def run_AI():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+song)
        pwk.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is '+time)
    elif 'tell me about' in command:
        query = command.replace('tell me about', '')
        info = wikipedia.summary(query, 2)
        print(info)
        talk(info)
    elif 'who is' in command:
        query = command.replace('who is', '')
        info = wikipedia.summary(query, 2)
        print(info)
        talk(info)
    elif 'good morning' in command:
        talk('good morning sir')
    else:
        talk('hmmm....I don''t know that')
        run_AI()

intro()

while True:
    run_AI()