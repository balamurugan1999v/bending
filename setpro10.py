lent=int(input())
a=input().split()
s1=[]
co=0
for i in a:
  s1.append(int(i))
for i in range(lent):
  for j in range(1,s1[i]):
    co=j+co
print(co)
