a=(input())
l1=len(a)
l=[]
if l1<= 100000:
	for i in a[::-1]:
		l.append(i)
s='-'.join(l)
print(s)
