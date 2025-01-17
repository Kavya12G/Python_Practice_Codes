'''
1. In tuples we can store homogenious as well as heterogenious data.
2. In tuples we can store duplicates.
3. Tuples are ordered collection of data.
4. Tuples are immutable.
'''
t1 = (10, 22.34, 'Kodnest', True, 10)
print(t1)
# t1.remove(10)
# t1.pop()
# del t1[2]
print(t1[2]) #Kodnest

#Deletes the complete tuple object
# del t1
# print(t1) #error

t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)#(1, 2, 3, 4, 5, 6)

# Create a Singleton Tuple:
t1 = (10,)
print(t1, type(t1))

new_t = (10, 20, 30, 40)
#ele1 = new_t[0]
#ele2 = new_t[1]

#Unpacking of tuple
ele1, ele2, ele3, ele4 = new_t
print('Value of ele1:', ele1)