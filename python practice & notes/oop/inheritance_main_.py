
# Example of OOP before using heritance 

class employee:
        salary = 1000
        age = 15
        standard = 10

rudi = employee()
print(rudi.age, rudi.standard, rudi.salary)


class programmer:
        salary = 50
        age = 15
        standard = 10

rudi = programmer()
print(rudi.age, rudi.standard, rudi.salary)

# With heritance 

# Explaination :
# Below there, I've created a class employee with some information about them. 

# But What if? Again i want to print the same class? 
# copying code will take years!! 

# So Now we use heritance as shown in line 40 with a class programmer. 

class employee:
        salary = 1000
        age = 15
        standard = 10

rudi = employee()
print(rudi.age, rudi.standard, rudi.salary)

#  Example of heritance 1

class programmer(employee):
        salary = 50
        age = 10
        standard = 10
rudi = programmer()
print(rudi.age, rudi.standard, rudi.salary)


#  Example of heritance 2 

class crickter(employee):
        salary = 6700

rudi = crickter()
print(rudi.age, rudi.standard, rudi.salary)


#  Multilevel Inheritance 

class bowler():
        bowlertype = 'pacer'
        avgspeed = 100
        economy = 7.5
        overall = 'Decent'


b = bowler.bowlertype, bowler.avgspeed, bowler.economy

class batsman():
        batsmantype = 'Opener'
        avgruns = 50
        strikerate = 137.56
        overall = 'Good'

c = batsman.batsmantype, batsman.avgruns, batsman.strikerate

# Example of multiple inheritance 

class allrounder(batsman, bowler):
        pass

print(b, c)


# Example of super ()

class Millennials():
        def __init__(self):
            print("Millennials are the pure Tradition :")
        birth_range = '1981-1996'


class GenZ(Millennials):
        def __init__(self):
            super().__init__()
            print("Gen-z is the pure nostaligia :")
        birth_range2 = '1997-2012'
        

class GenAlpha(GenZ, Millennials):
        def __init__(self):
            super().__init__()
            print("GenAplha is the pure brain rot <sub3 :")
        birth_range3 = '2013-2024'

# function call -!! 
m = GenAlpha()
print(m.birth_range3)



# Class methods

# If u want to  

class subvalue():
       a = 1
       @classmethod
       def show(cls):
              print(f"The Attribuurte a has value {cls.a}")

        
cbse = subvalue()
cbse.a = 45

cbse.show()


