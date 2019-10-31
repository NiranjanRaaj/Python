n=int(input())
if n<=100000:
	l=list(input().split())
	lim=1
	t=0
	for i in l:
		c=l.count(i)
		if c>lim:
			a=t
			lim=c
		t=t+1
	print(l[a])
			