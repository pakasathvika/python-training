n=input()

upper,lower,special,digit=1,1,1,1
if 8-len(n)>4:
    print(8-len(n))
else:
    for i in n:
        if(i.isalpha() and i.isupper()):
            upper=0
        elif(i.isalpha() and i.islower()):
            lower=0
        elif not i.isalnum():
            special=0
        elif(i.isdigit()):
            digit=0
    sum=upper+lower+special+digit
    if sum>0:
        print(sum)
    else:
        print(-1)
    
    

            
            

    