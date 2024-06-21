'''a=[5,8,9,5,2,4,7]
if len(a)%2==0:
    print("yes")
else:
    print("no")'''
    
nums=[4,7,5,2,3]
s=sum(nums)
x=0
r=[]
for i in nums:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r)

#another method
nums=[4,7,5,2,3]
s=sum(nums)
x=0
r=[]
j=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(nums)


