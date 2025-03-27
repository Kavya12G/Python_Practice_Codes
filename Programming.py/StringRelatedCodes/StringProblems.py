# #Reverse String
# s = input()
# res = s[::-1]
# print(res)

# #Palindrome Check
# s = input()
# res = s[::-1]
# if res == s:
#     print("Yes, is Palindrome")
# else:
#     print("No, is not Palindrome")

#Anagram or not
# s1 = input()
# s2 = input()
# if sorted(s1)==sorted(s2):
#     print("are Anagrams")
# else:
#     print("are not Anagrams")

#   #or using counter(): its countes occurance of each character

# from collections import Counter
# s1 = input()
# s2 = input()
# if Counter(s1) == Counter(s2):
#     print("yes, are anagrams")
# else:
#     print("no, are not anagrams")

#First non-repeating character
from collections import Counter
s = input()
s1 = ""
char_count = Counter(s)
for char in s:
    if char_count[char] == 1:
        print(s1 + char)
        break
else:
        print("-1")


    

