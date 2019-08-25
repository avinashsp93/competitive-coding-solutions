# 2. Even Fibonacci Numbers
# Language: Python 3
# Testcases: 5/5

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib = []
    a = 1
    fib.append(a)
    b = 1
    fib.append(b)
    next_num = a+b
    fib.append(next_num)
    while(next_num < n):
        a = b
        b = next_num
        next_num = a+b
        fib.append(next_num)
        if(next_num >= n):
            break
    sum_fib = 0
    for i in range(2,len(fib),3):
        if(fib[i] < n):
            sum_fib+=fib[i]
    print(sum_fib)
