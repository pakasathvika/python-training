'''def remove(s):
    stack=[]
    for char in s:
        if char=='*':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
s="leet**cod*e"
r=remove(s)
print(r)'''

s="leet**cod*e"
b=[]
for i in s:
    if(i!='*'):
        b.append(i)
    else:
        b.pop()
print(''.join(b))


#1859 sorting the sentence
#ip: "is2 snetence4 This1 a3"
#op:This is a sentence

