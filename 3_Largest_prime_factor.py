#https://www.hackerrank.com/contests/projecteuler/challenges/euler003
t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    ans = 1
    while(n%2==0):
        ans = 2
        n = n/2
    p=3
    while(p<=n**0.5):
        while(n%p==0):
            ans = p
            n = n/p
        p = p+2
    if(n>ans):
        ans = n
    print ans
