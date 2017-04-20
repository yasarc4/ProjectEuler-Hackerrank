#https://www.hackerrank.com/contests/projecteuler/challenges/euler025
first = 1
second = 1

prev_len = 1
digits = [0]*5001
digits[1]=1
i = 2
while(prev_len <5000):
    i = i+1
    third = first + second
    first = second
    second = third
    if(len(str(third)) > prev_len):
        digits[prev_len+1]=i
        prev_len = prev_len+1

t = int(raw_input().strip())
for i in range(t):
    n = int(raw_input().strip())
    print digits[n]
