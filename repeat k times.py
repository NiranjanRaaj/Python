a,b=(int(x) for x in input().split())
if (a<= 100000)and(b<= 100000):
	l=list(input().split())
	t=[]
	s=''
	r=0
	for i in l:
		c=l.count(i)
		if c==b:
			t.append(i)
			r=1
	t=list(dict.fromkeys(t))
	s=' '.join(t)
	if r==1:
		print(s)
	else:
		print(-1)
		