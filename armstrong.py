def armstrong(n):
  c=0
  for i in str(n):
    t=int(i)
    c=c+(t**3)
  if n==c:
    print (n," is an armstrong number")
  else:
    print (n," is not an armstrong number")

num=int(input("enter the number:"))
armstrong(num)
