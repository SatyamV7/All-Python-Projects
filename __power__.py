import math
int('0b100', base=0)
inp = int(input("Enter a number:- "))
root = int(input("You want to root till which power of number you entred:- "))
exec = math.pow(inp, (1/root))
answer = round(exec)
print(inp,"is",answer,"to power root",root)
displayroot = u'\u00broot'
print(displayroot,"√",inp,"=",answer)