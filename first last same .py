n=int(input())
l=list(input().split())
s1=0
s2=0
for i in l[0:3]:
	i=int(i)
	s1=s1+i
for j in l[n-1:n-4:-1]:
	j=int(j)
	s2=s2+j
if s1==s2:
	print(1)
else:
	print(0)
	
