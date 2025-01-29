class Calculator:
    def calculate(self,a,b):
        pass

class Add(Calculator):
    def calculate(self,a,b):
        print("Addition:",a+b)

class Sub(Calculator):
    def calculate(self,a,b):
        print("subtraction:",a-b)

class Mul():
    pass

ref = Add(10,20)
ref.calculate()


ref = Sub(10,20)
ref.calculate()


ref = Mul(10,20)
ref.calculate()