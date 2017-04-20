#https://www.hackerrank.com/contests/projecteuler/challenges/euler016
def sum_digits(x):
    s = 0
    while(x>0):
        s= s + (x%10)
        x=x//10
    return s

t = int(raw_input().strip())

for i in range(t):
    n = int(raw_input().strip())
    print (sum_digits(2**n))
