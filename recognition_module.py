import encodings.idna

import speech_recognition as sr
global count
count = 0

def recorder():
    global count
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        count +=1
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
#        print("Text: "+r.recognize_google(audio_data, language = "ta-IN"))


