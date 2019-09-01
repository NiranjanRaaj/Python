n=int(input())
s=str(n)
t=0
if n<=10000000000:
	for i in s:
		i=int(i)
		if (i%2)!=0:
			t=t+i
	if((t%2)==0):
		print("E")
	else:
		print("O")