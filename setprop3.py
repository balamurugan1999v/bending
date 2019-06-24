sen1,sen2=input().split()
co=0
a=len(sen1)
b=len(sen2)
if a<b:
  for i in range(a):
    if sen1[i]!=sen2[i]:
      co+=1
  d=b-a
  ans=d+co
else:
  for i in range(b):
    if sen1[i]!=sen2[i]:
      co+=1
  d=b-a
  ans=d+co
print(ans)
