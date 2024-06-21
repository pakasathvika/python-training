''' ip:
        "hello : 5438, car : 214, book : 8799, apple : 2187"
         lenght of hello - 5
         check whether is 5 present in that number or not, if present() print "o"
         car - 3 was not there, so, take next smallest number -that is '2'-"a"
         if smallest no. was also not present print "x"
    op:
        oaxp '''
a=input().split(',')
s=''
for i in a:
    b=i.split(":")
    l=len(b[0])
    if(str(l) in b[1]):
        s=s+b[0][-1]
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                s=s+b[0][i-1]
                break
        else:
            s=s+'x'
print(s)
    
    