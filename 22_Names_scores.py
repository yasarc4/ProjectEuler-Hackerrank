#https://www.hackerrank.com/contests/projecteuler/challenges/euler022
names = []
t = int(raw_input().strip())
for i in range(t):
    temp = raw_input().strip()
    names.append(temp)
names.sort()
values = []
for name in names:
    temp = 0
    for letters in name:
        temp = temp + ord(letters) - 64
    values.append(temp)
values = [values[i]*(i+1) for i in range(len(values))]
q = int(raw_input().strip())
for query in range(q):
    name = raw_input().strip()
    ans = [values[i] for i in range(len(values)) if names[i]==name]
    print ans[0]
