s=input()
sr=' '.join(s)
li=sr.split(' ')
lis=len(li)
l=len(s)
if l<= 10000000:
	for i in  range(0,lis,2):
		li[i],li[i+1]=li[i+1],li[i]
	sr=''.join(li)
	print(sr)