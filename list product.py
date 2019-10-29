n=int(input())
p=1
if n<=100000:
	l=list(input().split())
	for i in l:
		p=p*int(i)
	if p%2==0:
		print('even')
	else:
		print('odd')
		