# 4. Largest Palindrome Product
# Language: Python 3
# Testcases: 3/4

T = int(input())
while(T!=0):
    N = int(input())
    l = []
    zee = 0
    l_lim = int(N/999)
    for i in range(l_lim,1000):
        for j in range(i,1000):
            prod = i*j
            if(str(prod)==str(prod)[::-1] and prod<N and prod>zee):
                zee = prod
            elif(prod>N):
                break
    print(zee)
    T-=1