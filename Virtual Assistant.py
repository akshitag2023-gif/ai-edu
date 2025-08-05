import pyttsx3
import datetime

def print_and_speak(text):
    print(text)
    text_to_speech_convertor.say(text)
    text_to_speech_convertor.runAndWait()

text_to_speech_convertor = pyttsx3.init()

text = "My name is Ether"

print_and_speak(text)

text = "I am your Virtual Assistent"

print_and_speak(text)

current_hour = int(datetime.datetime.now().hour)

if current_hour < 12:
    text = "Good Morning, Sir"
elif current_hour < 17:
    text = "Good Afternoon, Sir"
else:
    text = "Good Evening, Sir"

print_and_speak(text)

'''while True:
    text = input("Enter the text you want to convert into speech(Enter s to stop): ")

    if text == 's':
        break

    print_and_speak(text)'''
    


if current_hour < 12:
    text = "Have a good day, Sir"
elif current_hour < 17:
    text = "Have a good afternoon, Sir"
elif current_hour < 19:
    text = "Have a good evening, Sir"
else:
    text = "Good Night, Sir"

print_and_speak(text)
    

