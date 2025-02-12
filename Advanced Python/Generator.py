def fibonacci_gen(num):
    a, b = 0,1
    for i in range(num):
        yield a
        print(a)
        a,b = b, a+b

ref = fibonacci_gen(1000)
print(next(ref)) #0
print(next(ref)) #1

# for i in range(5):
#     print(next(ref))