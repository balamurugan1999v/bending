s1=[]
a=int(input())
for i in range(a):
  t=input().split()
  for j in t:
    s1.append(int(j))
s1.sort()
for i in range(len(s1)):
  print(s1[i],end=" ")
