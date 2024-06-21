''' ip:	n=12
        k=2
    factors of n: 1,2,3,4,6,12
    op: 6 '''
def kth_largest_factor(n, k):

    factors = [i for i in range(1, n + 1) if n % i == 0]
    factors.sort(reverse=True)
    return factors[k - 1]


n = 12
k = 2
print(kth_largest_factor(n, k)) 

    

    





        
    