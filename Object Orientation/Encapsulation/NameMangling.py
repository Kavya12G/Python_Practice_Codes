class Demo1:
    def __init__(self, name):
        self.__name = name #Private Variable
    
d1 = Demo1('Akash')

'''
1. NameMangling is the process of Providing new name to the private variables.
2. These new names will be provided automatically by python for all private members.

new Name will be providede in format:
objectName.__className__variableName
'''