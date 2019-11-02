l,r,n=(int(x) for x in input().split())
if (1<=l<=100000)and(1<=l<=100000)and(1<=l<=100000):
	c=0
	for i in range (l,r+1):
		i =str(i)
		if str(n) in i:
			c=c+1
	print(c)