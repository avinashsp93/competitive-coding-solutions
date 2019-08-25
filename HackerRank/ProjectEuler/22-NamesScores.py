# 22. Names Scores
# Language: Python 3
# Testcases: 2/2

N = int(input())
names_list = []
for i in range(0,N):
    names_list.append(input())
names_list.sort()
Q = int(input())
while(Q!=0):
    name = input()
    sum = 0
    for i in name:
        sum+=ord(i)-64
    print((names_list.index(name)+1)*sum)
    Q-=1