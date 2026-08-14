# basic syntax 
if(n := len(input('Enter your name: '))) > 4:
    print(f'name is too long ({n} characters)')

# Exercise 1 : 

#  This code asks a user to guess a secret number. It checks the guess and saves it at the same time

# secret_number = 7
# guess = int(input("Guess the number (1-10): "))
# if guess == secret_number:
    # print(f"Correct! {guess} is the magic number.")
# else:
    # print(f"Wrong! {guess} is not correct.")

# 💡 Hint: Combine the guess = int(...) line into the if statement line.

secret_number = 6
if(guess := int(input("Guess the number (1-10): "))) == secret_number:
    print(f'Correct! {guess} is the magic number.')
else:
    print(f"Wrong! {guess} is not correct.")

