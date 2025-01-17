#Find Runner-up Score
l1 = list(map(int, input().split()))
l1 = list(set(l1))
l1.sort(reverse = 'True')
print(l1[1])
