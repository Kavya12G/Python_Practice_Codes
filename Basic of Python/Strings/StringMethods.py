#Different ways of Declaring the strings
s1 = "I'm Kavya"
s2 = 'My "Age" is 23'
s3 = """We are Learning
        Strings"""
s4 = '''Python is Dynamically
        Typed Language'''
print(s1)
print(s2)
print(s3)
print(s4)


# def find_pairs(nums, target):
#     nums.sort()
#     a = set()
#     res = set()

#     for num in nums:
#         b = target - num
#         if b in a:
#             res.add(tuple(sorted((num, b))))
#         a.add(num)

#     return [list(pair) for pair in res]

# nums = [1,1,2,2,3,3]
# target = 5
# print(find_pairs(nums, target))