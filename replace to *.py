import  math
s=input()
t=list(s)
l=len(s)
if l%2==0:
	m=l//2-1
	n=m+1
	t[m]='*'
	t[n]='*'
	s=''.join(t)
	print(s)
else:
	m=l/2-1
	m=math.ceil(m)
	t[m]='*'
	s=''.join(t)
	print(s)
	
	