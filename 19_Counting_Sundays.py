#https://www.hackerrank.com/contests/projecteuler/challenges/euler019/
t = int(raw_input().strip())
from datetime import date
from datetime import timedelta

def y400():
    start_date = date(1,1,1)
    stop_date = date(401,1,1)
    #print (stop_date)
    addn = 6 - start_date.weekday()
    ans = 0
    start_date = start_date + timedelta(addn)
    while(start_date <= stop_date):
        #print start_date
        if (start_date.day==1):
            ans = ans+1
        start_date = start_date+timedelta(days=7)
    return ans

s_400 = y400()

for ax in range(t):
    y,m,d = map(int,raw_input().strip().split())
    y1,m1,d1 = map(int,raw_input().strip().split())

    if(y%400 > 0):
        no_400s = y//400
        no_400s = no_400s*400
    else:
        no_400s = y//400 - 1
        no_400s = no_400s*400

    diff_400s = (y1-y)//400
    diff = (y1 - y)%400

    start_date = date(y-no_400s,m,d)
    stop_date = date(y-no_400s+diff,m1,d1)
    addn = 6 - start_date.weekday()
    ans = 0
    start_date = start_date + timedelta(addn)
    while(start_date <= stop_date):
        if (start_date.day==1):
            ans = ans+1
        start_date = start_date+timedelta(days=7)
    ans = diff_400s*s_400 + ans
    print ans
