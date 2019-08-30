N=int(input())
L,R=[int(x) for x in (input().split())]
if N in range(L,R+1):
	print('yes')
else:
	print('no')