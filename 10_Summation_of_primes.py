#https://www.hackerrank.com/contests/projecteuler/challenges/euler010
def is_prime(x):
    flag = 1
    for i in range(3, int(x**0.5)+1, 2):
        if(x%i == 0):
            flag = 0
            break
    return flag

primes = [2,3]

for i in range(5,1000000,2):
    if(is_prime(i)==1):
        primes.append(i)

ans = [2]
for i in range(1,len(primes)):
    ans.append(ans[i-1]+primes[i])

def find(x, start, stop):
    if (x==primes[int((start+stop)/2)]):
        return int((start+stop)/2)
    elif (stop-start<=1):
        if(primes[start]>x):
            return start-1
        elif(x>primes[stop]):
            return stop
        else:
            return start
    elif (x>primes[int((start+stop)/2)]):
        return find(x,int((start+stop)/2),stop)
    else:
        return find(x,start,int((start+stop)/2))

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print ans[find(n,0,len(primes)-1)]
