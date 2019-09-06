a=int(input())
c=0
for i in range(2,a):
	if (a%i)==0:
		c=0
	else:
		c=1
if c==0:
	print('yes')
else:
	print('no')