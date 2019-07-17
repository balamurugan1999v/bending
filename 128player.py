b=int(input())
a=input().split()
s1=[]
temp=0
for i in a:
  s1.append(int(i))
  if int(i)%2==0:
    temp=1
if temp==1:
  print("even")
else:
  print("odd")
