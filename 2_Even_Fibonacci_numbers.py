#https://www.hackerrank.com/contests/projecteuler/challenges/euler002/
t = int(raw_input().strip())

series = [1,2]

f = 1
s = 2
temp = 3

while(temp <= 4 * 10**16):
    series.append(temp)
    f = s
    s = temp
    temp = f+s

series = [series[i] for i in range(len(series)) if series[i]%2==0]
l = len(series)

for a0 in xrange(t):
    n = long(raw_input().strip())
    x = [series[i] for i in range(l) if series[i]<=n]
    print sum(x)
