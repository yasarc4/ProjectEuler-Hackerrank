#https://www.hackerrank.com/contests/projecteuler/challenges/euler017/
dic_ones = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',8:'Eight',9:'Nine', 10:'Ten', 11:'Eleven',
            12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen', 19:'Ninteen'}
dic_tens = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninty'}

def words(x):
    ans = ''
    hundred_exist = 0
    ten_exist = 0
    if(x//100 > 0):
        ans = ans + dic_ones[x//100] + ' Hundred'
        hundred_exist = 1
    x = x%100
    if (x==0):
        return ans
    ans = ans + ' '
    if(dic_ones.has_key(x)):
        ans = ans + dic_ones[x]
    else:
        ans = ans + dic_tens[x//10]
        x = x%10
        ten_exist = 1
        if(x>0):
            ans = ans + ' ' + dic_ones[x]
    return ans

t = int(raw_input().strip())
for i in range(t):
    ans = ''
    n = int(raw_input().strip())
    if(n==0):
        print 'Zero'
        next
    else:
        trillions = n//1000000000000
        n=n%1000000000000
        billions = n//1000000000
        n=n%1000000000
        millions = n//1000000
        n = n%1000000
        thousands = n//1000
        n = n%1000
        if(trillions>0):
            ans = ans+'One Trillion '
        if(billions>0):
            ans = ans + words(billions) + ' Billion '
        if(millions>0):
            ans = ans + words(millions) + ' Million '
        if(thousands>0):
            ans = ans + words(thousands) + ' Thousand '
        if(n>0):
            ans = ans + words(n)
        j=1
        while(j<len(ans)):
            if(ans[j]==' ') and (ans[j-1]==' '):
                ans = ans[:j]+ans[j+1:]
            else:
                j = j+1
        print ans.strip()
