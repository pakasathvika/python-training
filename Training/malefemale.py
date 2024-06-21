
'''str="mmmfffmmffffmfmmfmf"
c=0
count=0
for i in str:
    if i=='m':
        count+=1
        
    else:
        c+=1
        
if count==c:
    print(0)
elif count>c:
    print('m')
else:
    print('f')

'''str="mfmfmfmfmfmfmmff"
c=0
for i in str:
    if i=='m':
        c=c+1
    else:
        c=c-1'''