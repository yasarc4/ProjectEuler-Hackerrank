#https://www.hackerrank.com/contests/projecteuler/challenges/euler006
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    square_sum = n*(n+1)*(2*n+1)/6
    sum_square = (n*(n+1)/2)**2
    print sum_square-square_sum
