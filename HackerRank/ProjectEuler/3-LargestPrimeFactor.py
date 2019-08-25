# 3. Largest Prime Factor
# Language: Python 3
# Testcases: 4/6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while(n%2 == 0):
        n//=2
    hf = 0
    pf = 1
    for i in range(3,n//3,2):
        if(n%i == 0):
            n//=i
            hf = i
    pf = max(hf,n)
    print(pf)