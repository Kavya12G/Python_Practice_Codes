s = 'Kodnest1234*'
print(s.isalnum()) #False

print('Kodnest12'.isalpha()) #False
print('code'.isalpha()) #True

print('12'.isdigit()) #True

print(any(True, False, False))
print(any(False, False, False))

#----------real code logic-------------------
s = input()
print(any([i.isalnum() for i in s])) #True
print(any([i.isalpha() for i in s])) #True
print(any([i.isdigit() for i in s])) #True
print(any([i.islower() for i in s])) #True
print(any([i.isupper() for i in s])) #True
