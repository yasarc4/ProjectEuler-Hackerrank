#https://www.hackerrank.com/contests/projecteuler/challenges/euler013
n = int(raw_input().strip())
ans = long(0)
for i in range(n):
    x = long(raw_input().strip())
    ans = ans+x
print str(ans)[:10]
