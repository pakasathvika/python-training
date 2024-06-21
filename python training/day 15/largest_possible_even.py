''' ip:
        tu5g2k1h8                        take unique number(without repitation)-521863
        g5g8gd6h3                        with this 521863 make largest possible even number
    op:
        865312   largest possible even number '''

'''def ud(s1, s2):
    s=s1+s2
    d=set()
    for char in s:
        if char.isdigit():
            d.add(char)
    return sorted(d,reverse=True)
def l_e_d(digits):
    even=[d for d in digits if int(d)%2==0]
    odd_digits=[d for d in digits if int(d)%2!=0]
    if not even:
        return "Not possible"
    largest_number=''.join(digits)
    smallest_ed=even[-1]
    largest_number=largest_number.replace(smallest_ed,'',1)+smallest_ed
    return largest_number
s1="tug22k1h8"
s2="g5g8gd6h3"
d=ud(s1,s2)
largest_even=l_e_d(d)
print(largest_even) '''


a="tu5g2k1h8"
b="g5g8gd6h3"
c=set()
for i in a:
    if i.isdigit():
        c.add(i)
for i in b:
    if i.isdigit():
        c.add(i)
d=list(sorted(c,reverse=True))
if(int(d[-1])%2==0):
    print(''.join(d))
else:
    for i in range(len(d)-2,-1,-1):
        if(int(d[i])%2==0):
            d.append(d.pop(i))
            print(''.join(d))
            break
        else:
            print(-1)
           
    


