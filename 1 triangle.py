n=int(input())
if n<=1000:
	t='1'
	for i in range(1,n+1):
		print(t)
		t=t+' 1'+' 1'
	