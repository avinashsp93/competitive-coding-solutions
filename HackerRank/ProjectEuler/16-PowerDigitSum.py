# 16. Power Digit Sum
# Language: Python 3
# Testcases: 10/10

T = int(input())
while(T!=0):
    N=int(input())
    bigN=str(int(pow(2,N)))
    sum=0
    for i in bigN:
        sum+=int(i)
    print(sum)
    T-=1