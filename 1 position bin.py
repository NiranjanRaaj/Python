a=int(input())
b=bin(a)
b=b.replace('0b','')
c=1
for i in b[::-1]:
	if i=='1':
		print(c)
		break
	c=c+1
  
	