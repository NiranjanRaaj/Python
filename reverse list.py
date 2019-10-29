n=int(input())
s=''
if 1<=n<=10000:
	l=list(input().split())
	l.sort(reverse=True)
	s='->'.join(l)
	print(s)
	