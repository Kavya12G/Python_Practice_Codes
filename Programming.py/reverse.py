l1 = [10,20,30,40]
print("Before reverse:", l1) #[10, 20, 30, 40]
l1.reverse()
print("After reverse:", l1) #[40, 30, 20, 10]

#list(reversed(object)):
l2 = [11, 3, 5, 8]
reverse_l2 = list(reversed(l2))
print(l2) #[11, 3, 5, 8]
print(reverse_l2) #[8, 5, 3, 11]

l3 = [1,5,2,9]
new_reverse_l3= list(reversed(l3)) #-->Creating new reverse list
l3.reverse() #--->Reversing Original List