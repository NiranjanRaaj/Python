s=input()
l=len(s)
if  1 <= l <= 100000:
	l=list(s)
	l=list(dict.fromkeys(l))
	s=''.join(l)
	print(s)