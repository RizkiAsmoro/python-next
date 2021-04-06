'''
Voice Translation
'''
# instal pip googletrans and speech_recognition
# 1 recognition the source voice as text 
# 2 translate text to destination and print

from googletrans import Translator
import speech_recognition as voice

x = voice.Recognizer()
y = Translator()

with voice.Microphone() as source:
    x.adjust_for_ambient_noise(source)
    print("Speak Anything now to translate:")
    audio = x.listen(source)
    try:
        text = x.recognize_google(audio)
        result = y.translate(text, dest='jw')
 #       print("You said : {}".format(text))
        print (result.text)        
    except:
        print("Sorry could not recognize what you said")