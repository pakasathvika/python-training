''' palindrome or not
    if not print the nearest palindrome number
    ip:
        122
    op:
        131
    ---------
    ip:
        1234
        12 34
        1221 /\
    op:
        1331(increment 2 and mirror it )
    ---------
    ip:
        56472
        56 472
        56465/\
        (increment middle value and mirror it)
    op:
        56565
    ---------
    ip:
        12412
        12 412
        12421
    op:
        12421
    ----------
    #return str(num) == str(num)[::-1]'''

#def is_palindrome(n):
'''n = int(input("Enter a number: "))
rev=0
t=n
while(t!=0):
    r=t%10
    rev=(rev*10)+r
    t=t//10
if(rev==n):
    print("palindrome")
else:
    n += 1  
    while not(t!=0):
        n += 1
    print(n)'''

    
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def next_greatest_palindrome(num):
    num += 1
    while not is_palindrome(num):
        num += 1
    return num
n = int(input("Enter a number: "))
next_palindrome = next_greatest_palindrome(n)
print(f"The next greatest palindrome after {n} is {next_palindrome}.")

