# map(function,iterable_obj)
l = [1,2,3,4]

def double(num):
    return num * 2

double_l=list(map(double, l))
print(double_l) #[2, 4, 6, 8]

# filter(function,iterable_obj)
def checkEven(num):
    return num % 2 == 0
even_l = list(filter(checkEven, l))
print(even_l) #[2, 4]

# reduce
from functools import reduce
def mul(a,b):
    return a * b
res = reduce(mul, l)
print('Multiplication is:', res) #24