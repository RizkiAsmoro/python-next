'''
Translation 
First, pip install googletrans
and makesure the latest googletranslate mod

'''
from googletrans import Translator
x = Translator()
result = x.translate('selamat malam', dest='en')
print (result.text)
