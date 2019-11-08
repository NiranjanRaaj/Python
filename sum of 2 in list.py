n,x=(int(x) for x in input().split())
if n<= 100000 and x <= 100000:
	l=list(input().split())
	t=0
	for i in l:
		c=0
		i=int(i)
		for j in l[c+1:]:
			j=int(j)
			if j+i==x:
				t=1
				break
		c=c+1
		if t==1:
			break
	if t==1:
		print('yes')
	else:
		print('no')
		