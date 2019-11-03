n,k=(int(x) for x in input().split())
wait=0
for i in range (1,n):
	t=10
	w=t-k
	wait=wait+w
print(wait)

''' 2nd method

n,k=(int(x) for x in input().split())
c=n-1
w=10-k
wait=c*w
print(wait)



In a garage the service man takes 10 minutes to service one car.If there are N cars in garage and X is number of minutes after which one person arrives,Calculate how much time last person has to wait in garage.(Print answer in minutes
	