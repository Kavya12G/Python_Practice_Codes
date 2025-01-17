'''
1. In Set we can store homo and heterogeneous type of data.
2. Set is an unordered collection of data.
3. set will not allow Duplicates.
4. Set does not support indexing of data.
5. Sets are mutable.
'''
s1 = {10, True, 'Kodnest', 20, 54.87, 10}
print(s1, type(s1)) #{True, 20, 54.87, 10, 'Kodnest'}
# print(s1[0]) # error

#add(): Used to add an element in the set.
s1.add(500)
print(s1) #{True, 'Kodnest', 20, 500, 54.87, 10}

s1.remove(54.87)
print(s1) #{True, 'Kodnest', 20, 500, 10}

#pop(): Without index will delete one ele and return.
poped_ele = s1.pop()
print(poped_ele) #True
print(s1) #{'Kodnest', 20, 500, 10}