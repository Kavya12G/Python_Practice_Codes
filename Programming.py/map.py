# map(function, iterable_object)

def double(x):
    return x*2

l1 = [1,2,3,4]
double_l2 = list(map(double, l1))
print(double_l2) #[2, 4, 6, 8]

tup = ('10', '20', '30')
print(tup) #('10', '20', '30')
tup = tuple(map(int, tup))
print(tup) #(10, 20, 30)

l2 = [1,3,56]
print(l2) #[1, 3, 56]
l2 = list(map(float, l2))
print(l2) #[1.0, 3.0, 56.0]