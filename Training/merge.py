def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergesort(left)
        right=mergesort(right)
        #print(left,right)
        mergedl=merge(left,right)
        return mergedl
    return l
def merge(left,right):
    res=[]
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
l=list(map(int,input().split()))

#[3,9,8,1,0]
print(mergesort(l))
            