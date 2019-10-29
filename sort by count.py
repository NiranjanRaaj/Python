n,m=(int(j) for j in input().split())
l=list(input().split())
x=[]
y=''
if(n<=100000)&(m<=100000):
	for i in l:
		c=l.count(i)
		if c<m:
			x.append(i)
	x.sort()
	y=' '.join(x)
	print(y)
	
	
	