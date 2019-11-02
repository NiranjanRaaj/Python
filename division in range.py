n=int(input())
if n<= 100000:
	l=list(input().split())
	i=max(l)
	while True:
		i=int(i)
		for j in l:
			j=int(j)
			if i%j==0:
				c=1
				continue
			else:
				c=0
				break
		if c==1:
			s=i
			break
		else:
			i=i+1
			continue
	print(s)
		
		
		