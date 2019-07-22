a=input()
s2=[]
for i in range(len(a)-1):
  c=0
  if a[i]=='a' and a[i+1]=='b':
    c+=2
    i=i+2
    #print(i)
    while(i<len(a)):
      if a[i]!='a':
        i=i+1
        break
      elif a[i]=='a':
        c+=1
        i=i+1      
      if i<len(a):
        if a[i]=='b':
          c+=1
          i=i+1
        elif a[i]!='b':
          i=i+1
          break
  #print(c) 
  s2.append(c)
s2.sort()
#print(s2)
print(s2[-1])
