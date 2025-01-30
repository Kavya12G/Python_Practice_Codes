nums1 = [1,2,2,1] 
nums2 = [2,2]
l = []
n1 = list(set(nums1))
n2 = list(set(nums2))
for i in n1:
    if i in n2:
        l.append(i)
print(l)

