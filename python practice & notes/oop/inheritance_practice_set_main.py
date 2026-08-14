#  1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvector():
    def __init__(self, i, j):
        self.i = i 
        self.j = j 

    def output(self):
        print(f"The I vector is {self.i} and j vector is {self.j}")

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 

    def output(self):
        print(f"The vector i is {self.i}, The vector j is {self.j}, The vector k is {self.k}") 


x = twoDvector(1, 2)
x.output()

y =threeDvector(5, 6, 7) 
y.output()




# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.



class Animals():
    def __init__(self, dog):
        self.dog = dog    


class Pets(Animals):
    def __init__(self, dog):
        super().__init__(dog)

    def show():
        print(f"Animals like dog has features like bhao bhao ")


a = Animals()
a.dog()

b = Pets()
b.show()
