n = int(input())
d = {}
for i in range(n):
    name, *score = input().split()
    scores = list(map(float, score))
    d[name] = scores
target = input()
if target in d:
   avg = sum(d[target])/3
print(f"{avg:.2f}")

