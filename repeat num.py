N=int(input())
if 1 <= N <= 100000:
	l=list(input().split())
	t=[]
	r=0
	for i in l:
		c=l.count(i)
		if c>=2:
			t.append(i)
			r=1
	t.sort()
	t=list(dict.fromkeys(t))
	s=' '.join(t)
	if r==1:
		print(s)
	else:
		print('unique')