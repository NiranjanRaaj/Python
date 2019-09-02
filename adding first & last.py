a=int(input())
if a<=1000000000000000:
	s=str(a)
	l=len(s)
	t=int(s[0])+int(s[l-1])
	print(t)