n=int(input())
if  2 <= n <= 100000:
	l=[]
	for i in range(1,n+1):
		c=1
		if n%i==0:
			c=0
			for j in range (2,i//2+1):
				if i%j==0:
					c=c+1
					break
		if c==0 and i!=1:
			l.append(str(i))
	s=' '.join(l)
	print(s)
		
		