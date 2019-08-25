# 13. Large Sum
# Language: Python 3
# Testcases: 3/3

N = int(input())
big_add = []
sum = 0
for i in range(0,N):
    big_add.append(int(input()))
    sum+=big_add[i]
print(str(sum)[0:10])
