import webbrowser

import speech_recognition as sr
import os
import openai
import datetime
from config import api_key
import random

chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = api_key
    chatStr += f"Anıl : {query}\n Jarvis"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[],
            temperature=1,
            prompt=chatStr,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        print(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
        # if not os.path.exists("OpenAI"):
        #     os.mkdir("OpenAI")
        # with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        #     f.write(text)
    except Exception as e:
        print(str(e))
        say("Sorry sir I can not help you")
def ai(prompt):
    openai.api_key = api_key
    text = f"OpenAI response for Prompt: {prompt}\n ******************** \n\n"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("OpenAI"):
            os.mkdir("OpenAI")
        with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
            f.write(text)

    except Exception as e:
        say("Sorry sir I can not help you")

def say(text):
    os.system(f"say {text}")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="tr-TR")
            print(f"You said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"

if __name__ == '__main__':
    say("Hello I am JarvisAI")
    while True:
        print("Listening...")
        query = take_command()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],  ["facebook", "https://www.facebook.com"],  ["instagram", "https://www.instagram.com"],   ["twitter", "https://www.twitter.com"],  ["linkedin", "https://www.linkedin.com"],   ["github", "https://www.github.com"],  ["stackoverflow", "https://www.stackoverflow.com"],  ["reddit", "https://www.reddit.com"],  ["medium", "https://www.medium.com"],  ["quora", "https://www.quora.com"],  ["stackoverflow", "https://www.stackoverflow.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "play music".lower() in query.lower():
            music_path = "/Users/anilduyguc/Documents/Python/JarvisAI/musics"
            files = os.listdir(music_path)
            files = [file for file in files if os.path.isfile(os.path.join(music_path, file))]
            if files:
                random_file = random.choice(files)
                os.system(f"open {music_path + '/' + random_file}")

            # import subprocess, sys
            # opener = "open" if sys.platform == "darwin" else "xdg-open"
            # subprocess.call([opener, music_path])

        elif "the time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/Facetime.app")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            say("Bye sir")
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr += ""
        else:
            chat(query)

