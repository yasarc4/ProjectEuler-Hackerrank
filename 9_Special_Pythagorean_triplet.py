#https://www.hackerrank.com/contests/projecteuler/challenges/euler009
t = int(raw_input().strip())
for a0 in xrange(t):
    ans = -1
    n = int(raw_input().strip())
    if (n%2 == 1):
        print ans
        continue
    # a = x2-y2   |   b = 2xy    |    c = x2+y2    |    x>y     |     sum = 2x2 + 2xy      |     prod = 2xy * (x2-y2) * (x2+y2)
    for i in range(2,int((n/1.4)**0.5)+2):
        for j in range(1,i):
            sum_abc = 2*i*i + 2*i*j
            if(sum_abc>n):
                break
            if (n%sum_abc == 0):
                ans1 = 2*i*j*(i*i - j*j)*(i*i + j*j)* (n/sum_abc)**3
                if(ans1>ans):
                    ans=ans1
    print ans
