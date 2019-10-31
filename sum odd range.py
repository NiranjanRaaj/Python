x,y=(int(c) for c in input().split())
o=0
for i in range(x,y+1):
	if i%2 != 0:
		o=o+i
print(o)