#https://www.hackerrank.com/contests/projecteuler/challenges/euler001/
t = int(raw_input().strip())
for a0 in xrange(t):
    n = long(raw_input().strip())
    n = n-1
    m_3 = long(n//3)
    m_3 = m_3*(m_3+1)*3/2
    m_5 = long(n//5)
    m_5 = m_5*(m_5+1)*5/2
    m_15 = long(n//15)
    m_15 = m_15*(m_15+1)*15/2
    ans = m_3 + m_5 - m_15
    print ans
