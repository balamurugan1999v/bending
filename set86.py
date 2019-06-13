a=input()
s1=[]
for i in a:
  s1.append(i)
b=len(s1)
co=0
for i in range(b):
  for j in range(i+1,b):
    if s1[i]==s1[j]:
      co=1
      break
  if co==1:
    break
if co==1:
  print ("no")
else:
  print("yes")
