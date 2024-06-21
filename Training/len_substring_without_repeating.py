'''
  length of substring without repeating characters\
  ip:
      abfgresagtyuiofde
  op:
      12
      '''
a="abfgresagtyuiofde"
d={}
s=""
m=0
i=0
while(i<len(a)):
    if(a[i] not in s):
        s=s+a[i]
        d[a[i]]=i
    else:
        if(len(s)>m):
            m=len(s)
        s=""
        i=d[a[i]]
    i=i+1
print(m)
