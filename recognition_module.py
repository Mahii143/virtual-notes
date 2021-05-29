#import encodings.idna
import os
import speech_recognition as sr
global text
def recorder():
    global text
    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        print("Recognizing...")
        
        # convert speech to text
        text = r.recognize_google(audio_data)
        


recorder()
file = open("mahir.pdf",'w+')
file.writelines(text)
file.close()


