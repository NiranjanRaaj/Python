a=int(input())
if a<=1000:
	b=[]
	for i in range (a):
		b.insert(i,input())
	s=min(b,key=len)
	print(s)