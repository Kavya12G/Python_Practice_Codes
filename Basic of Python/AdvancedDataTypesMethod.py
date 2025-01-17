#list(iterable_object)
l1 = list('Kod')
print(l1) #['K', 'o', 'd']

l2 = list ((10,20))
print(l2) #[10, 20]

l3 = list ({100,200})
print(l3) #[200, 100]

l4 = list ({'name':'Kavya', 'age':10})
print(l4) #['name', 'age']

l5 = list(range(1, 10))
print(l5) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#tuple(iterable_object)
t1 = tuple([10,20])
print(t1) #(10, 20)
t2 = tuple({100, 200})
print(t2) #(200, 100)
t3 = tuple(range(1, 11))
print(t3) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t4 = tuple('Kodnest')
print(t4) #('K', 'o', 'd', 'n', 'e', 's', 't')
t5 = tuple({'name':'Kavya', 'age':10})
print(t5) #('name', 'age')

#set(iterable_object)
s1 = set([10,20,30,10])
print(s1) #{10, 20, 30}

#dict(iterable_object:key:value)
d1 = dict([['name','Priya'],['age',22]])
print(d1) # {'name': 'Priya', 'age': 22}
