l = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    l.append([name, score])

scores =[]
for name, score in l:
    scores.append(score)
    scores = list(set(scores))
    scores.sort()

name_list = []
second_largest = scores[1]
if scores == second_largest:
    name_list.append(name)
    name_list.sort()
for name in name_list:
    print(name)
