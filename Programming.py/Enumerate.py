'''1. Write python program to print all even index elements.
'''
li = list(map(int, input("Enter numbers separated by spaces: ").split()))
for idx, ele in enumerate(li):
    if (ele % 2 == 0):
        print(idx, ele)