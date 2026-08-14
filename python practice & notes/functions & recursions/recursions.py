# Example of factorial 

'''
factorial(n) 
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 * 1 = 6
factorial(4) = 4 * 3 * 2 * 1 = 24
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

factorial(n) = n * n-1 * ....... 3*2*1

| Therefore |
factorial(n) = n * factorial(n-1)

'''

# example of recursions and factorial

def factorial(n):
    if(n==0 or n == 1):
        return 1
    return n * factorial(n-1)

user_num = int(input('Enter a number for factorial '))

print(f'The factorial of the number {user_num} is ({factorial(user_num)}) : ')
