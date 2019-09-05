s=input()
l=len(s)
s1=input()
lis=[]
c=0
if l<= 1000000:
	lis=s.split(' ')
	c=lis.count(s1)
	print(c)
	
	