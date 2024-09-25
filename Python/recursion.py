# write a recersive function to print the sum of n natural number

def naturalSum(n):
    if(n==1): return 1
    else: return n + naturalSum(n-1)
print(naturalSum(10))