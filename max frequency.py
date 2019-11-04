s=input()
le=len(s)
if  1 <= le <= 100000:
	l=list(s)
	m=max(set(l), key=l.count)
	print(m)