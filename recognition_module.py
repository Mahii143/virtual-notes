#import encodings.idna
import os
import speech_recognition as sr
from datetime import datetime
from datetime import date

today = date.today()
#print("Today's date:", today)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_time1 = str(today)+str(current_time)

def recorder():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=10)
        #print("Recognizing...")
        
        # convert speech to text
        text = r.recognize_google(audio_data)
        #print("user said: {0}".format(text))


        #os.remove("mahir.txt")
        file = open("mahir.pdf",'w+')
        
        file.writelines(current_time1)
        file.writelines("\n")
        file.writelines(text)
        file.writelines("\n")
        file.close()


