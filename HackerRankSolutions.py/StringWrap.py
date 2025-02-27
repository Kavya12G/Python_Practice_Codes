import textwrap

def stringwrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

string = input()
max_width = int(input())
print(stringwrap(string, max_width))