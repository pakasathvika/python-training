''' coprimes or not '''
a=3
b=9

for i in range(2,(min(a,b)//2)+1):
    if(a%i==0 and b%i==0):
        print("ncp")
        break
else:
    print("cp")

