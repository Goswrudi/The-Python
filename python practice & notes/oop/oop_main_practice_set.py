# Now We're solving some problems 


# 1. Create a class “Programmer” for storing information of few programmer1s working at Microsoft.

class programmer1:
    organisation = "Microsoft"
    languages_For_OS  = "C & C++"
    languages_For_AI = "Python & JavaScript"
    Avg_Package = 4000000 
    Emviorment = "10/10"

employee_microsoft = programmer1()
print(programmer1.organisation, programmer1.languages_For_OS, programmer1.languages_For_AI, programmer1.Avg_Package, programmer1.Emviorment)

# Sorry guyssss The problem says fro a "FEW PROGRAMMER1 "

class programmer:
    Company = "Microsoft"
    
    def __init__(self, name , Avg_Package, Enviorment):
        self.name = name
        self.Avg_Package = Avg_Package
        self.Enviorment = Enviorment

p = programmer("Rudransh", "36lpa", '10/10')
print(p.name, p.Avg_Package, p.Enviorment)


#  2. Write a class “Calculator” capable of finding square, cube and square root of a number

class Calculator:
    def Square(self):
        i = int(input('Enter a number : '))
        solution = i ** 2
        return solution
    
    def Cube(self):
        i = int(input('Enter a number : '))
        solution = i ** 3
        return solution
    
    def SquareRoot(self):
        i = int(input('Enter a number : '))
        solution = i ** 0.5
        return solution

    @staticmethod
    def greet():
        print('Hlo!') 
        return 

Calculator.greet()

my_calc = Calculator()
solution1 = my_calc.Square()
print(f'The solution is {solution1}')
    
my_calc = Calculator()
solution2 = my_calc.Cube()
print(f'The solution is {solution2}')

my_calc = Calculator()
solution3 = my_calc.SquareRoot()
print(f'The solution is {solution3}')

 
#  3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Myclass:
    a = 10


obj = Myclass()

obj.a = 0

print(f'Solution of class is {Myclass.a} : ') 
print(f'Solution of class is {obj.a} :')


# 4. Add a static method in problem 2, to greet the user with hello. 

# Added the static method 

# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint 

class Train:

    def __init__(self, trainno):
        self.trainno = trainno

    def Ticket(self, food, start, end):
        print(f"The Train no {self.trainno} has {food} type , It started frm {start} and will end on {end}")


    def Status(self, start, end):
        print(f'The Status of train no {self.trainno} which started from {start} and will end on {end} ')

    
    def fare(self):
        print(f"The fare of train no {self.trainno} is {randint(67, 450)}") 


info = Train(676767)
info.Ticket("Indian food", "Delhi", "Ghaziabad")
info.Status("Delhi", "end")
info.fare()



