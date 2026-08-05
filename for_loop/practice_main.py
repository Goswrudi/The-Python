#  The While loops Paradox
i = 0

while(i<5):
    print('Jai Modi')
    i += 1

# Counting in for loop

for i in range(5):
    print('Namste Bharat')


# Counting with fix variable in for loops 

j = 16
for j in range(j):
    print(j)

# Counting in for loop with random numbers

import random
k = random.randint(1 , 12)
for k in range(k):
    print(k)


# For loops can also be used for step sizzing 

for a in range(0 , 100 , 4):
    print(a) 
    # In a way it also printed the table of 4 but with reach of 100

# Iteration in loops 

p = ['apple' , 'mangos', 'kiwi']
for o in p:
    print(o)

# For loop with else

p = ['apple' , 'mangos', 'kiwi']
for o in p:
    print(o)
else:
    print('done')

# For loop with break 

for l in range(100):
    if(l == 11):
        break
    print(l) 
