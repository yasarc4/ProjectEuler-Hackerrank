#https://www.hackerrank.com/contests/projecteuler/challenges/euler028/
t = int(raw_input().strip())

for ax in range(t):
    n = int(raw_input().strip())
    ans1 = (n*(n+1))/2
    ans1 = ans1%1000000007
    ans2 = (n*(n+1)*(2*n+1))/6 - n*n
    ans2 = ans2%1000000007
    x = (n+1)/2
    ans3 = (2*x*(2*x - 1)*(2*x + 1)/3) - 1 - (n*n + 1)/2
    ans3 = ans3%1000000007
    print (ans1+ans2+ans3)%1000000007
