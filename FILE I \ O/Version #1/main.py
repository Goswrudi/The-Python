'''
1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it
contains the word ‘twinkle’.

'''

p = open('poem.txt')
content = p.read()
if('twinkle' in content):
    print('The word twinkle is avaible at file poem.txt')

else:
    print('The word twinkle is not avaible at file poem.txt')