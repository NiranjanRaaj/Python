a,b=[str(x) for x in input().split()]
if((len(a)<=10000)&(len(b)<=1000))==True:
	if b in a:
		print('yes')
	else:
		print('no')