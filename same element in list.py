a=int(input())
if a<=1000:
	l=[]
	c=0
	for i in range (a):
		l.append(input())
	for x in l:
		if l.count(x)>=2:
			c=1
	if c!=1:
		print('no')