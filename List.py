'''
1. In list we can store homogenious as well as heterogenious data.
2. Duplicate values allowed.
3. List is an ordered collection of data.
4. Lists are mutable(modify or change).
'''
l1 = [10,20,30.45,True,'Kodnest']
print(l1, type(l1))

#append(): will add element at end of the list
l1.append(300) 
print(l1)

#insert(index, element): add element at perticular index.
l1.insert(1, 12)
print(l1)

#remove(element): remove 1st occurance of the specified element.
l1.remove(12)
print(l1)

#in and not in Operator:
print(2000 in l1) #False
print('Kodnest' in l1) #True

#pop(): without argument will delete last elm from list and return.
remove = l1.pop()
print(remove) #300
print(l1) #[10, 20, 30.45, True, 'Kodnest']

#pop(index): with argument will delete elm at specified index
remove = l1.pop(4)
print(remove) #Kodnest
print(l1) #[10, 20, 30.45, True]

#del Keyword:
del l1[1]
print(l1) #[10, 30.45, True]

del l1
print(l1) #error