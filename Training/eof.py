a=input().split()
sum_e=0
sum_o=0
sum_f=0.0
for i in a:
    if(i.isdigit()):
        n=int(i)
        if n%2==0:
            sum_e+=n
        else:
            sum_o+=n
    elif '.' in i:
        n=float(i)
        sum_f+=n
print(sum_e,sum_o,sum_f)
        