# How to clear punctuation in string
punctuation = '''!@#$%^&*()_+="~<>,.{}|\[]?/:'''
#string = 'Hello !!!, from Indonesia :)'
string = str (input('try here :'))
no_puc = ""
for char in string:
    if char not in punctuation:
        no_puc = no_puc + char
print ('clear puctuation:',no_puc)
