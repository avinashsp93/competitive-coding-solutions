# 20. Factorial Digit Sum
# Language: Python 3
# Testcases: 4/4

T = int(input())
while(T!=0):
    N = int(input())
    prod = 1
    sum = 0
    for i in range(1,N+1):
        prod*=i
        if(prod%10==0):
            prod = int(prod)//10
    for i in str(prod):
        sum+=int(i)
    print(sum)
    T-=1