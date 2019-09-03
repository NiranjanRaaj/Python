a=int(input())
l=[]
t=0
if 1<=a<=100000:
	l=input().split()
	for i in l:
		if int(i)<a:
			print(i)
