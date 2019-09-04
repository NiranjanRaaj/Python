a=int(input())
b=[]
b=(input().split())
l=len(b)
for  i in range (1,l,2):
	b[i],b[i-1]=b[i-1],b[i]
x=' '.join(b)
print(x)