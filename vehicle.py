def namedetails():
    n=str(input("Enter Your Name: "))
    for i in n:
      if i.isdigit() or ord(i) not in range(65,123):
        print("\nEnter correct details\n")
        return details()
        break
    return n
def numdetails():
  try:
    cdet=int(input("Enter Your Contact Number: "))
    return cdet
  except ValueError:
    print("\nEnter the correct details\n")
    return numdetails()

name=namedetails()
num=numdetails()

def slocation():
  try:
    s=float(input("Enter Source: "))
    if s<0:
     print("\nEnter positive source\n")
     return slocation()
  except:
    print("\nEnter the correct source\n")
    return slocation()
  return s

def dlocation():
  try:
    d=float(input("Enter Destination: "))
    if d<0:
      print("\nEnter positive destination\n")
      return dlocation()
  except:
    print("\nEnter the correct destination\n")
    return dlocation()
  return d
  
def call():
  s=slocation()
  d=dlocation()
  if d < s or d==s:
    print("Enter correct value")
    return call()
  else:
  	return s,d

source,destination=call()

km=destination-source
if km<0:
  km=km*(-1)

def vehicle():
  cat=input("Enter the Category bike or car or auto: ")
  cat.lower()
  if cat=="bike":
   c=km * 10
   return c,cat
  elif cat=="car":
   c=km * 30
   return c,cat
  elif cat=="auto":
   c=km * 20
   return c,cat
  else:
    print("enter bike or car or auto")
    return vehicle()

cost,v=vehicle()

print("\n\nINVOICE""\nNAME:",name,"\nNUMBER:",num,"\nSOURCE:",source,"\tDESTINATION:",destination,"\nvechicle:",v,"\nTOTAL Km:",km,"km","\nCOST:",cost,"rs")
