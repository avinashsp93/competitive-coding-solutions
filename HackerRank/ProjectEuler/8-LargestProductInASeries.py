# 8. Largest product in a series
# Language: Python 3
# Testcases: 10/10

T = int(input())

while(T!=0):
    line = input().strip().split()
    N = int(line[0])
    K = int(line[1])
    max_prod = 0
    digit = input()
    for i in range(0,len(digit)-K):
        prod = 1
        for j in range(i,i+K):
            prod *= int(digit[j])
        if(prod>max_prod):
            max_prod = prod
    print(max_prod)
    T-=1