print("\nNormal Pattern:")
n=int(input("enter the number:"))
for i in range (0,n,1):
  for j in range(0,i+1):
    print("*",end=" ")
  print("")

print("\ninverted Pattern:")
n=int(input("enter the number:"))
for m in range (n,0,-1):
  for k in range(0,m):
    print("*",end=" ")
  print("")

print("\nfull Pattern:")
n=int(input("enter the number:"))
for i in range (0,n,1):
  for j in range(0,i+1):
    print("*",end=" ")
  print("")
for m in range (n,0,-1):
  for k in range(0,m):
    print("*",end=" ")
  print("")

print("\nfull Pattern 2:")
n=int(input("enter the number:"))
for i in range (0,n,1):
  for j in range(0,i+1):
    print("*",end=" ")
  print("")
for m in range (n-1,0,-1):
  for k in range(0,m):
    print("*",end=" ")
  print("")

print("\ndiamond Pattern :")
n=int(input("enter the number:"))
r=n-1
r2=1
l=[]
for i in range (0,n,1):
  l.append("*")
  s=" ".join(l)
  print(r*" ",s)
  r=r-1
  #print("")
for m in range (n-1,0,-1):
  s=" ".join(l[:m])
  print(r2*" ",s)
  r2=r2+1
  if r2==n:
    break
  #print("")