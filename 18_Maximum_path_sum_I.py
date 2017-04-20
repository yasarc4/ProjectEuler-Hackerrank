#https://www.hackerrank.com/contests/projecteuler/challenges/euler018
t = int(raw_input().strip())

def no_paths(levels):
    ans = []
    for i in range(2**levels):
        binary="{0:b}".format(i)
        while(len(binary)<levels):
            binary = '0'+binary
        ans.append(binary)
    return ans

for ix in range(t):
    n = int(raw_input().strip())
    li = []
    for j in range(n):
        li.append(map(int, raw_input().split()))

    paths = no_paths(n-1)
    ans = 0
    for path in paths:
        temp = li[0][0]
        pos = 0
        for i in range(1,n):
            pos = pos + int(path[i-1])
            temp = temp + li[i][pos]
        if(temp>ans):
            ans = temp
    print ans
