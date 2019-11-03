n=int(input())
if 1 <=n<= 1000:
	l=[]
	for i in range (1,n+1):
		if n%i==0:
			if i%2!=0:
				l.append(str(i))
	s=' '.join(l)
	print(s)