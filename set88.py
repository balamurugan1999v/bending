a1,b1=input().split()
a=int(a1)
b=int(b1)
c=0
if a<b:
  t=a
  a=b
  b=t
d=a*b
#print(a,d+1)
for i in range(a,d+1):
  if (i%a)==0 and (i%b)==0:
    c=i
    break
print(c)
