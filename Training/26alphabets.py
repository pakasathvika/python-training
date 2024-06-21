''' check whether the string has all 26 alphabets or not.
    ip:
        "the quick brown fox jumps over the lazy dog"
    op:
        yes
    ------------------------------------
    ip:
        "qwweer yuiop asdfvgh JKL mnbvlkjcxz"
    op:
        no 
    ------------------------------------ '''

'''a= "qwweer yuiop asdfvgh JKL mnbvlkjcxz"
s=set(a)
c=0
for i in s:
    c+=1
print(a)
if(c==27):
    print("yes")
else:
    print("no") '''

'''a=input()
for i in range(97,123):
    if(chr(i) not in a):
        print("no")
        break
else:
    print("yes")   '''

a=input()
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]=1
print(d)
    
    
