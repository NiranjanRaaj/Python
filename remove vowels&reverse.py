n=int(input())
v=['a','e','i','o','u','A','E','I','O','U']
if (1<=n<=100000)==True:
	a=input()
	c=''
	for x in a:
		if x==' ':
			c=c+x
		elif(x not in v):
			c=c+x
	print(c[::-1])
	
		