'''
1. for control_variable in iterable_object'''

# for-Loop

for i in 'Kodnest':
    print(i)

for j in [10,20,30,40]:
    print(j+2)

for num in range(1,11):
    print(num)

print()

for num in range(11, 21, 2):
    print(num, end=" ")

print()

for i in range(5):
    print(i, end=" ")

print()

#WAP to print all  even numbers from 1-10
for num in range(1, 11):
    if (num%2 == 0):
        print(num, end=" ")

# while Loop

i = 0
while(i < 10):
    print(i+100)
    i=i+1

#WAP to print numbers from 1-10 if number is 6 then skip printing
for i in range(1, 11):
    if (i == 6):
        continue
    print(i)

print()

#WAP to print numbers from 11-21 if number is 15 then stop printing
for i in range(11, 21):
    if (i == 15):
        break
    print(i)