#https://www.hackerrank.com/contests/projecteuler/challenges/euler007
def is_prime(x):
    flag=0
    for i in range(3,int(x**0.5+1),2):
        if(x%i == 0):
            flag=1
            break
    if(flag == 0):
        return 1
    else:
        return 0

t = int(raw_input().strip())
primes=[0,2,3,5]
for i in range(7,105000,2):
    if(is_prime(i)==1):
        primes.append(i)

for a0 in xrange(t):
    n = int(raw_input().strip())
    print primes[n]
