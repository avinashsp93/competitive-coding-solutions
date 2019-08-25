# 6. Sum Square Difference
# Language: Python 3
# Testcases: 2/2

T = int(input())
while(T!=0):
    N = int(input())
    print((N*(N+1)*(N-1)*(3*N+2))//12)
    T-=1