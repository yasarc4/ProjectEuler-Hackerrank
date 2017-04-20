#https://www.hackerrank.com/contests/projecteuler/challenges/euler008
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = str(raw_input().strip())
    max_prod = 0
    for i in range(k,n):
        prod = 1
        for j in range(i-k, i):
            prod = prod*int(num[j])
        if(prod>max_prod):
            max_prod = prod
    print max_prod
