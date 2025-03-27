# def sumOfDigits(st):
#     num_str = ''.join(str(ord(char)-ord('a')+1)for char in st)
#     num = sum(int(digit) for digit in num_str)
#     return num
# st = "zyvf"
# res = sumOfDigits(st)
# print(res)



# # missing numbers in list

# lst = [1,2,3,4,7,8,9]
# complete = set(range(1, len(lst)))
# present = set(lst)
# res = list(complete - present)
# print(res)


str = "11"
str2 = "1"
ash = bin(int(str,2) + int(str2, 2))
print(ash[2:])