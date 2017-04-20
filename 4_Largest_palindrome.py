#https://www.hackerrank.com/contests/projecteuler/challenges/euler004/
def palin(x):
    x1=x
    rev = 0
    while(x>0):
        rev = rev*10 + (x%10)
        x = int(x/10)
    if(x1==rev):
        return 1
    else:
        return 0
palins = []
for i in range(100,1000):
    for j in range(i,1000):
        temp = i*j
        if(palin(temp)==1):
            if(not(temp in palins)):
                palins.append(temp)

t = int(raw_input().strip())
l = len(palins)
for a0 in xrange(t):
    n = int(raw_input().strip())
    temp1 = [palins[i] for i in range(l) if palins[i]<n]
    print max(temp1)
