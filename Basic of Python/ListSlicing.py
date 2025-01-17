#List_name[start:end:steps]

l1 = [10,20,30,40,50,60]
sub_list1 =l1[::]
print(sub_list1) #[10, 20, 30, 40, 50, 60]

sub_list2 =l1[1::]
print(sub_list2) #[20, 30, 40, 50, 60]

sub_list1 =l1[::2]
print(sub_list1) #[10, 30, 50]

reverse_list = l1[::-1]
print(reverse_list) #[60, 50, 40, 30, 20, 10]

reverse_list1 = l1[-1::]
print(reverse_list1) #[60]

'''
Q: What is slicing?
Is used to create sublist from main list.
Syntax: list_name[start, end, steps]

reverse list: [::-1]
last ele: [-1::]
'''