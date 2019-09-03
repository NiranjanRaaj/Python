a=int(input())
l=[]
t=0
if 1<=a<=100000:
	l=input().split()
l.sort(reverse=True)
t=int(''.join(l))
print(t)
