def swapCase(s):
    sample = ''
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    return sample
res = swapCase("PUYhgd")
print(res)