li = list(map(int,input().split())) #[10,20,20,30]
d =  {}
for i in li:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for num, count in d.items():
    print(f"{num} occures {count} time(s)")
    

#---------------------------------------------------
d = {10:2, 20:1, 30:1}
for num, count in d.items():
    print(f"{num} occures {count} time(s)")

# num, count = (10, 2)
# num, count = (20, 1)
# num, count = (30, 1)

#packing-------------------------------------------------------
name , *marks, age = ['Kavya', 29,45,54, 23]
print(marks)
print(age)
