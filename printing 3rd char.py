x=input()
n=len(x)
s=''
for i in range (0,n):
	if (i==0)|(i==3)==True:
		s=s+x[i]
print(s)