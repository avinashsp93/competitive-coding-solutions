# 21. Amicable numbers
# Language: Python 3
# Testcases: 3/4

import math

factor_sum_dict = {}

def findFactorSum(n):
    factor_sum = 1
    for i in range(2, math.floor(math.sqrt(n))+1):
        if(n%i == 0):
            factor_sum+=i
            if(n//i != i):
                factor_sum+=(n//i)
    return factor_sum

for i in range(1, 100001):
    factor_sum_dict[i] = findFactorSum(i)

T = int(input())
while(T>0):
    N = int(input())
    
    count = 1
    amicable_sum = 0
    while(count <= N):
        v = factor_sum_dict[count]
        if(v != count and factor_sum_dict.get(v) == count):
            amicable_sum += count
        count+=1
    print(amicable_sum)
    T-=1