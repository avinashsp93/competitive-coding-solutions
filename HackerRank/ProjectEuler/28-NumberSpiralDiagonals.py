# 28. Number Spiral Diagonals
# Language: Python 3
# Testcases: 5/5

T = int(input())

while(T > 0):
    N = int(input())
    terms = (N+1)//2
    sq_summation = (terms*(2*terms+1)*(2*terms-1))//3
    sub_summation = (terms-1)*terms
    result = 4*sq_summation - 6*sub_summation - 3
    print(result%1000000007)
    T-=1
