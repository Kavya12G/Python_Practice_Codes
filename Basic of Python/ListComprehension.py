l1 = [1,2,3,4,5]
even = [i for i in l1 if i % 2 == 0]
sq_list = [i**2 for i in l1]
new_list = [i + 2 for i in l1]
print(even)
print(sq_list)
print(new_list)

even_odd = ['even' if i % 2 == 0 else 'odd' for i in l1]
print(even_odd)