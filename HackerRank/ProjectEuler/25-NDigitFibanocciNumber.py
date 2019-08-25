# 25. N-Digit fibonacci number
# Language: Python 3
# Testcases: 4/4

import math

T = int(input())
fib_digits = {}

def number_of_fibonacci_digits():
    n = 3
    a = 1
    b = 1
    while(n < 23930):
        c = a+b
        if(len(str(b)) < len(str(c))):
            fib_digits[len(str(b))+1] = n
        n+=1
        a = b
        b = c

number_of_fibonacci_digits()

while(T!=0):
    print(fib_digits[int(input())])
    T-=1