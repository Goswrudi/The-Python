class Unempolyeed:
    a = 1
    def show(self):
        print(f'This shows the class of ({self.a})')

e = Unempolyeed()
e.a = 12
print(e.a)

# But what if i want to show da real a which is 1 , we will  use @class method for that 

class Unempolyeed:
    a = 1
    @classmethod
    def show(cls):
        print(f'This shows the class of ({cls.a})')

e = Unempolyeed()
e.a = 12
e.show()
