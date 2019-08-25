# 1. Multiples of 3 and 5
# Language: Python 3
# Testcases: 6/6

def s(n): return n*(n+1)/2
def r(n): return s(n/3)*3 + s(n/5)*5 - s(n/15)*15
print('\n'.join(str(r(int(input())-1)) for i in range(int(input()))))