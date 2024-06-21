'''ip=f46feLK9y56u#&56hIjbn6KJhA
op:lv-2
uv-2
lc-
uc-
d-
s-
'''
a="f46feLK9y56u#&56hIjbn6KJhA"
lv,uv,lc,uc,d,s=0,0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uc+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1
    elif(not i.isalnum()):
        s=s+1
print(lv,lc,uv,uc,d,s)
    
    
