from functools import reduce 
l = [1,2,3,4,5]

new_l = list(filter(lambda num : num %2 == 0,l))
print(new_l)

sum = reduce(lambda a,b:a+b,l)
print(sum)

square = list(map(lambda num: num**2, l))
print(square)
