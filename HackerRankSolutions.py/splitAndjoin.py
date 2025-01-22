def splitAndjoin(line):
    line = line.split()
    return "-".join(line)

line = input()
res = splitAndjoin('This is a sample')
print(res)
