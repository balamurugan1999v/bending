s1=[]
a=int(input())
for i in range(a):
  y=input()
  s1.append(y)
b=s1[0]
for i in range(1,a):
  c=""
  mini=len(b) if len(b)<len(s1[i]) else len(s1[i])
  for j in range(mini):
    if b[j]==s1[i][j]:
      c+=b[j]
    else:
      break
  b=c[::1]
  #print(b)
  #print(c)
print(b)
