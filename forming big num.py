s=input()
t=len(s)
l=[]
x=''
if t<=10000000:
	for i in s:
		l.append(i)
	l.sort(reverse=True)
	x=''.join(l)
	print(x)
	
	
		