#https://www.hackerrank.com/contests/projecteuler/challenges/euler024/
def fact(x):
    ans = 1
    for i in range(1,x+1):
        ans = ans*i
    return ans
perms = [fact(i) for i in range(12,0,-1)]
x='abcdefghijklm'
t = int(raw_input().strip())
for ax in range(t):
    temp = x
    n = int(raw_input().strip())
    n = n-1
    order = []
    for i in perms:
        tmp = n//i
        n = n%i
        order.append(tmp)
    ans = ''
    for i in order:
        ans = ans + temp[i]
        #print ans
        temp = temp[:i]+temp[i+1:]
    ans = ans + temp
    print ans
