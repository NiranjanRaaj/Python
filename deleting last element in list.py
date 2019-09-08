a,b=[int(x) for x in input().split()]
if (a<=100000) & (b<=100000):
	u=[]
	l=list(input().split())
	le=len(l)
	le=le-b
	for i in l[0:le]:
		u.append(i)
	t=' '.join(u)
	print(t)