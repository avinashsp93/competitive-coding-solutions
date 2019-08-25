# 18. Maximum Path Sum
# Language: Python 3
# Testcases: 6/6

T = int(input())
while(T!=0):
    l = []
    N = int(input())
    for i in range(0,N):
        l.append([int(k) for k in input().strip().split(' ')])
    for i in range(N-1,-1,-1):
        for j in range(0,i):
            l[i-1][j]+=max(l[i][j],l[i][j+1])
    print(l[0][0])
    T-=1