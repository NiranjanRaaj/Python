n=int(input())
if n<=1000000:
	l=list(input().split())
	m=min(l)
	m2=max(l)
	print(int(m2)-int(m))