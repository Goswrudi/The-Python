# Trying to solve some For loops problem 

# Problem 1 : Exercise 1: Feed the Zoo Animals (Warm-up)We have a list of hungry animals. Write a loop that loops through the list and prints: "Feeding the Lion", then "Feeding the Elephant", and so on.Your Basket: animals = ["Lion", "Elephant", "Monkey", "Penguin"]Hint: Look back at our very first apple basket example!

def feedinganimals():
    animals = ["Lion", "Elephant", "Monkey", "Penguin"]
    for feed in animals:
        print(f'feeding {feed}')

feedinganimals()


'''
Problem 2 : Create a while loop which will print the contetn of a list  
'''

lst = ['rudi' , 'sparsh', 'arjun', 'ayush']

i = 0

while(i < len(lst)):
    print(lst)
    i += 1