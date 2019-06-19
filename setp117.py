a=input()
a1=a[::-1]
b=len(a1)
for i in range(b-1):
    print(a1[i],end="-")
print(a1[-1])
