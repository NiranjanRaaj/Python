a,b=[int(x) for x in input().split()]
gcd=0
if a>b:
	l=b
else:
	l=a
for i in range(1,l+1):
	if((a%i)==0)&((b%i)==0)==True:
		gcd=i
print(gcd)