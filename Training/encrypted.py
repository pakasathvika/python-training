'''ip: khoor
       3
       d
       42
       
   op: hello
       s
   '''
'''def decrypt(text,shift):
    str=""
    for char in text:
        shift_b=ord('a')
        str+=chr((ord(char)-shift_b-shift)%26+shift_b)
    return str
text=input()
shift=int(input())
print(decrypt(text,shift))'''


#
a='bvec'
b=4
c=b%26
d=''
for i in a:
    if((ord(i)-c)>=97):
        d+=chr(ord(i)-c)
    else:
        d+=chr(ord(i)-c+26)
print(d)