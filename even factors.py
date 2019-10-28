n=int(input())
x=[]
if 1<=n<=1000:
	for i in range(2,n+1,2):
		if n%i==0:
			x.append(str(i))
	t=' '.join(x)
	print(t)