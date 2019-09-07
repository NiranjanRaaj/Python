a=int(input())
b=list(input().split())
c=max(set(b), key=b.count)
print(c)