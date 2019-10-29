a=int(input())
l=[]
l2=''
if(1 <= a <= 100000):

	l=input().split()
	c=-1
	t=0
	for i in l:
		i=int(i)
		c=c+1
		if i==c:
			l2=l2+str(i)
			t=1
	if t==1:
		s=' '.join(l2)
		print(s)
	else:
		print('-1')