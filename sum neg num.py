n=int(input())
if n<=100000:
	l=list(input().split())
	c=0
	for i in l:
		i=int(i)
		if i <0:
			c=c+i
	print(c)