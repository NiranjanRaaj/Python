n,k=(int(x) for x in input().split())
if n<=100000 and k<= 100000:
	if n<k:
		m=n
	else:
		m=k
	s=0
	for i in range (1,m+1):
		if n%i==0 and k%i==0:
			s=i
	print(s)
		