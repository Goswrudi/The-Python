# # # # Create a python funtion to calculate the avgrage of three nums entered by the user.

# # function defination
# def avg():
#     a = int(input('Enter a number : '))
#     b = int(input('Enter a number : '))
#     c = int(input('Enter a number : '))
#     sum_avg = (a + b + c)/3
#     print(sum_avg) 

# # function call
# avg()


# # # # write a function to greet a user with 'have a good day'

# def greet():
#     user = input('Enter your name : ')
#     print(f'Hey {user} have a good day')

# greet()


# # #  write a function with argument to greet a user with their name and age

# def greetings(profession, name):
#     print('Have a good day ' + profession + name)


# greetings('Programmer ', 'rudransh goswami') 


# # 1. Write a program using functions to find greatest of three numbers.

# def great_num():
#     name = input('enter your name : ')
#     x = int(input('Enter a number : '))
#     y = int(input('Enter a number : '))
#     z = int(input('Enter a number : '))
#     if(x > y and x > z):
#         print(f'Hey {name}, the greatest of three nums you entred is {x}')
    
#     elif(y > x and y > z):
#         print(f'Hey {name}, the greatest of three nums you entred is {y}')

#     else:
#         print(f'Hey {name}, the greatest of three nums you entred is {z}')


# great_num()


# # 2. Write a python program using function to convert Celsius to Fahrenheit.

# def convert():
#     name = input('Enter your name : ')
#     celsius = int(input('Enter your Celsius temprature to convert it on Fahrenheit '))
#     solution = (celsius * 9/5 + 32)
#     print(f'''Hey {name} The Celsius Temprature you entered is {celsius}°C & it's conversion to Fahrenheit is {solution}''') 

# convert()

# # 3. How do you prevent a python print() function to print a new line at the end.

# print('hello', end='')
# print('world')


# # 4. Write a recursive function to calculate the sum of first n natural numbers.

# def recursive_func(n): 
#     if(n == 1 or n == 0):
#         return 1
    
#     else:
#         return n + recursive_func (n-1)

# solution = recursive_func(79)
# print(solution)

# # 5. Write a python function to print first n lines of the following pattern.
# #  ***
# #  **.
# #  *
# # - for n = 3

# def pattern_recursive(n):
#     if( n == 0):
#         return 
#     else:
#         print('*' * n)
#         pattern_recursive(n-1)

# pattern_recursive(3)


# 6. Write a python function which converts inches to cms.
# formula : multiply the length value by 2.54

# def inches():
#     name = input('Enter your name : ')
#     inch_input = int(input("Enter the  inches to convert it into cms : "))
#     solution = (inch_input * 2.54)
#     print(f'hey {name}! {inch_input} inchs into cms are {solution} ')

# inches()

# 7. Write a python function to remove a given word from a list and strip it at the same time.
l = ['rudi', 'akku', 'ladoo', 'lol']

def remove(l, word):
    for item in l:
        l.remove(word)
        return l
    
print(remove(l, 'rudi'))


# 8. Write a python function to print multiplication table of a given number.

def multiplication(n):
    for i in range(1, 11):
        print(f'{n} X {i} = {n*i}')

multiplication(3)

