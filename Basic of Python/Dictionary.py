d1 = {'name':'Priya', 'age': 27, 'phone':23456}
print(d1, type(d1))

#In dict cannot store duplicate keys.
d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'age': 27, 'phone': 23456}

#In dict we can store duplicate values.
marks = {'Sci': 85, 'Maths': 85} #Allowed

for i in d1.keys():
    print(i)

for i in d1.values():
    print(i)

for i in d1.items():
    print(i)