n=int(input())
if 1<=n<=100000:
	l=list(input().split())
	l1=l
	l1.sort()
	if l==l1:
		print('yes')