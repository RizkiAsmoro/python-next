'''
Reverse
'''


#Reverse Array
print ('\n=======Reverse Array======')
n = [1, 2, 3, 4, 5]
for i in n :
    print (i, end=' ')
print ()
n = n[::-1]
for i in n:
    print(i, end=' ')


#Reverse string using 'Slicing'
print ('\n=======Reverse string using Slicing======')
x = 'abcdefghij'
print ('string  = abcdefghij',type(x))
print ('reverse =',x[::-1])

#Reverse String using 'reversed()'
print ('=======Reverse string using Reversed()======')
y = 'Hallo Python'
print ('String = Hallo Python',type(y))
print ('Reversed =',(''.join(reversed(y))))

#Reverse String using For loop
print ('=======Reverse string using For Loop======')
z = 'This is Python'
print ('String = This is Python')
for i in range(len(z)-1,-1,-1):
    print (z[i], end='')

#Reverse String using Recursion
print ('\n=======Reverse string using Recursion======')
def rev(c):
    if len(c)==0:
        return c
    else:
        return rev(c[1:])+ c[0]
    print(rev('Python is fun'))
