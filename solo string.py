s=input()
l=[]
for i in s:
	c=s.count(i)
	if c==1:
		l.append(i)
s=''.join(l)
print(s)