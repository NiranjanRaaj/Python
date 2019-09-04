a,b=[int(x) for x in input().split()]
p=a*b
c=0
if a==b:
	c=1
else:
	if a<=b:
		l=b
	else:
		l=a
	for i in range(l):
		if i*i==p:
			c=1
if c==1:
	print('yes')
else:
	print('no')