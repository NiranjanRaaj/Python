a,b=(int(x) for x in input().split())
if(a<=10000)and(b<=10000)and((a-b)<=5):
	af=1
	bf=1
	for i in range (1,a+1):
		af=af*i
	for j in range (1,b+1):
		bf=bf*j
	s=af//bf
	print(s)