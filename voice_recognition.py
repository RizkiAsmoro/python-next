'''
Voice Recognition
'''

import speech_recognition as voice
x = voice.Recognizer()
with voice.Microphone() as source:
    x.adjust_for_ambient_noise(source)
    print("Speak Anything now:")
    audio = x.listen(source)
    try:
        text = x.recognize_google(audio)
        print("You said : {}".format(text))       
    except:
        print("Sorry could not recognize what you said")
