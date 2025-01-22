def mutation(s, p, c):
    li = list(s)
    li[p] = c
    res = "".join(li)
    return res 
s = input()
p,c = input().split()
r = mutation("code",int(p),c)
print(r)