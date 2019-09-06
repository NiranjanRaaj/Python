a,b=[int(x) for x in input().split()]
c=a^b
d=str(bin(c))
print(d.count('1'))