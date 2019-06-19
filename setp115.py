a,b=input().split()
a1=len(a)
a2=len(b)
if a1<a2:
    c=a2-a1
    print(a+b[:a2-c])
elif a1>a2:
    c=a1-a2
    print(a[:a1-c]+b)
else:
    print(a+b)

