#https://www.hackerrank.com/contests/projecteuler/challenges/euler015
n = int(raw_input().strip())

for ax in range(n):
    x,y=map(int, raw_input().split())
    if (x>y):
        num = range(x+y,x,-1)
        den = range(2,y+1)
    else:
        num = range(x+y,y,-1)
        den = range(2,x+1)
    prod = num[0]
    for i in range(1,len(num)):
        if(len(den)>0):
            prod = prod * num[i]
            to_del = []
            for j in range(len(den)):
                if (prod%den[j]==0):
                    prod = prod/den[j]
                    to_del.append(den[j])
            for k in to_del:
                den.remove(k)
        else:
            prod = prod%1000000007
            prod = prod * num[i]

    print prod%1000000007
