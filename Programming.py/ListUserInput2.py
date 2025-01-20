l1 = input('Enter space separated elements ')
print(l1, type(l1)) #2 4 5 <class 'str'>
l1 = l1.split()
print(l1) #['2', '4', '5']
l1 = list(map(int, l1))
print(l1) #[4, 5, 7]

tup = list(map(int, input('Enter space seperated elements ').split()))
print([i for i in tup if i % 2 == 0])
    