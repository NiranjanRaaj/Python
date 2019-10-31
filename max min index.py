n=int(input())
if n<=100000:
	l=list(input().split())
	m=min(l)
	n=max(l)
	p=1
	t=[]
	for i in l:
		if i==m:
			p=str(p)
			t.append(p)
		p=int(p)+1
	q=1
	for j in l:
		if j==n:
			q=str(q)
			t.append(q)
		q=int(q)+1
	s=' '.join(t)
	print(s)