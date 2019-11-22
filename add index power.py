n=int(input())
s=str(n)
l=len(s)
t=0
if  1 <= n <= 100000:
  for i in range(0,l):
    t=t+int(s[i])**i
  print(t)
