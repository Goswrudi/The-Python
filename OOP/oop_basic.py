# Class : A class is like a big container in the code which create more resuablity of 
# Object :  A object is a variable reporudcing factor for the Class 
# 
# 
# Code Example 

class house:
    house_color = 'pinkish'
    house_size = 125 , 'M'
    house_area = 'NCR'

# Using Object to call class M1(stands for Model 1) 

M1 = house()
print(M1.house_area , M1.house_color , house.house_size)

class FamilyNature:
    sister = 'i wish'
    mother = 'kinda dumb'
    father = 'smart for that dumb mother'
    brother = 'ew !!'

    # default constructor 
    def __init__(self):
        print('Accesing databases ')

    # parameteriszed construtor
    def __init__(self, motherage, marks, character): # an init can handle as many arguments as our computer is capable for 
        self.age = motherage
        self.marks = marks 
        self.character = character
        print('ranking familymemebrs....')

FN = FamilyNature(45 , 89 , '10/10')
print(FN.age , FN.character , FN.marks)

# Okay So basically a lot of things happend at upper code and I'm explaining everything line by line 

# First we set variables name 
# then we use a constructor known 'init' (it has only be done for stop repetative writing of code )
# Now we have created init function ! but .. init function runs on two arguments ig --  so let us create the avriables for that || self var = mothervar , cause we want mother too gays --
# At the end just called the function kindly || hehe\
#
# another ai genrated examle is : 
# 
'''
class house:
    # This runs automatically during creation
    def __init__(self, color, size, area):
        self.house_color = color  # Attaches unique color to the object
        self.house_size = size    # Attaches unique size to the object
        self.house_area = area    # Attaches unique area to the object

# Creating unique objects instantly
M1 = house('blue', 125, 'NCR')
M2 = house('green', 200, 'Mumbai')

print(M1.house_color)  # Outputs: blue
print(M2.house_color)  # Outputs: green

''' 


# Methods in OOP 
# See what is a method ? , A Method is nothing but a function for oop 
# for eg : a way of doin

class M:
    @staticmethod
    def hello():
        print('hello ji ')

M.hello()
# # del keyword

# class rudransh:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age


# s1 = rudransh('rudransh goswami' , 12)
# print(s1.name , s1.age)

# del s1.name
# print(s1.name)

# Inheritance In OOP 
# there are many inheritances in oop :
# Single inheritance
# Multiple inheritance 
# Multilevel inheritance

# Single inheritance 

class Tech:
    def technology(self):
        print(f'cpu is a type of technology')

class TechComponents(Tech):
    
    def cpu(self):
        print('cpu are the core of all device')

T = TechComponents()
T.technology() 
T.cpu()

# super () method 

# you can use the super().__init__ method to calls the consturtor of the base class

