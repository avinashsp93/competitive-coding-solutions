# 5. Smallest Multiple
# Language: Python 3
# Testcases: 5/5

import math

T = int(input())
while(T!=0):
    N = int(input())
    sm = 1
    for i in range(1,N):
        sm = (sm*(i+1))/math.gcd(int(sm),i+1)
    print(int(sm))
    T-=1