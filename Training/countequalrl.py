#RLRRLLRLRL"-COUNT=4
s=input()
balance=0
count=0
for i in s:
    if i=="R":
        balance+=1
    else:
        balance-=1
    if balance==0:
        count=count+1
print(count)