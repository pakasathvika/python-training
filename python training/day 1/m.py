def merge(l1,l2):
    res=[]
    i=j=k=0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:
            res.append(l2[j])
            j+=1
    res.extend(l1[i:])         
    res.extend(l2[j:])
    '''while(j<len(b)):
            res.append(b[j])
            j=j+1
       while(i<len(a)):
            res.append(a[i])
            i=i+1
            '''
    return res
l1=[1,5,8,9]
l2=[2,7,9,10,14]

#[3,9,8,1,0]
print(merge(l1,l2))