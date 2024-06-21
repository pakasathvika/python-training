''' ip:
        "(([{}]))"
    op:
        -1
    ip:
        "[{()]]"
    op:
        5 '''
s="[{()]]"
st=[]
for i in s:
    if i=='(' or i=='{' or i=='[':
            st.append(i)
    else:
        if not st:
            print("false")
        elif i==']' and st[-1]=='[':
            st.pop()
        elif i=='}' and st[-1]=='{':
            st.pop()
        elif i==')' and st[-1]=='(':
            st.pop()
        else:
            print(s.index(i)+1)
            break
if not st:
    print("-1")
    

