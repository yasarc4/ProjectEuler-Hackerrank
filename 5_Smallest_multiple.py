#https://www.hackerrank.com/contests/projecteuler/challenges/euler005
def hcf(x,y):
    if(x<y):
        t=x
        x=y
        y=t
    if(x%y == 0):
        return y
    else:
        return hcf(y, x%y)

t = int(raw_input().strip())
n=[]
n.append(1)

for i in range(1,41):
    n.append(n[i-1]*i / hcf(i,n[i-1]))
    #print n
for i in range(0,t):
    n1 = int(raw_input().strip())
    print n[n1]
