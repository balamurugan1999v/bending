def digit(a):
  c=bin(a)
  v=0
  #print(a,c)
  d1=c[2:]
  d=int(d1)
  #print(int(d))
  while(d!=0):
    b=d%10
    if b==1:
      v+=1
    d=d//10
  #print(v)
  return v
s1=[]
s2=[]
b1=int(input())
a=input().split()
for i in a:
  s1.append(int(i))
if b1>1:
  fst=digit(s1[0])
  lst=digit(s1[1])
  #print(fst,lst)
  if fst>lst or ((fst==lst) and (s1[0]>s1[1])):
    s2.append(s1[0])
    s2.append(s1[1])
  else:
    s2.append(s1[1])
    s2.append(s1[0])
  #print(s2)
  for i in range(2,len(s1)):
    lst=digit(s1[i])
    #print(lst,s1[i])
    for j in range(len(s2)):
      fst=digit(s2[j])
      if fst<lst or((fst==lst) and (s1[i]>s2[j])):
        s2.insert(j,s1[i])
        break
        #print(s2)
    if (len(s2)!=i+1):
      s2.append(s1[i])
  for i in range(len(s2)):
    print(s2[i])
