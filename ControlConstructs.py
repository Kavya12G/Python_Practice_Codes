'''
1. Conditional: if-else, if-elif
2. Looping: for, while
3. Jumping: break, continue, pass
'''
def checkAge(age):
    if (age>18):
        print('Age id greater than 18')
    else:
        print('Age is not greater than 18')
checkAge(18)

def displayAgeCateg(age):
    if (age<18):
        print('child')
    elif(age >= 18 and age <=65):
        print('Adult')
    else:
        print('Senior')
displayAgeCateg(int(input('Enter age: ')))

