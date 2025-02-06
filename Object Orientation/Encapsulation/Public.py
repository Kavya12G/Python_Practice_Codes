'''Access modifiers are used to 
Determine the accessibility of data members and member function'''
class Demo1:
    def __init__(self, name):
        self.firstname = name
    def disp1(self):
        print(self.firstname)
d1 = Demo1('Akash')
print(d1.firstname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self.firstname)
d2 = Demo2('Pooja')
print(d2.firstname)
d2.disp2()
d1.disp1()

'''
The variable which are public, can be accessed inside the 
same class, outside of any class, insidethe child class, 
inside non-child class.'''