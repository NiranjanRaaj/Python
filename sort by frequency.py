n=int(input())
l=list(input().split())
m=sorted(set(l),key=l.count)
m=list(dict.fromkeys(m))
for i in m:
	print(i,end=' ')