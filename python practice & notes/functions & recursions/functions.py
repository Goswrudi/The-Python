
# This is just testing my skills in functions :) 

age = int(input('Enter your age : '))
gender = input('enter your gender : ').lower().strip()

def goon(age, gender):
    print(f'Your age is {age} and your gender is {gender}')

goon(age, gender)

if age >= 15 and gender == 'male':
    print('''You're gooner''')

elif age <= 10 and gender == 'male':
    print("No No you're not gooner")
 
elif age >= 15 and gender == 'female': 
    print('''You're gooner''')

elif age <= 10 and gender == 'female':
    print("No No you're not gooner") 

else:
    print("How i can know if you're gooner or not?") 

# recursions 
#  The defination :

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f"The factorial of the entered number is : {factorial(n)}") 

