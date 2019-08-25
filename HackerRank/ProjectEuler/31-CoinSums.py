# 31. Coin Sums
# Language: Python 3
# Testcases: 9/9


coin_types = 9
pound_max = 100001
coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]
T = int(input())

dp_matrix = [[0 for x in range(pound_max)] for y in range(coin_types)]
for i in dp_matrix:
    i[0] = 1

for i in range(1, len(dp_matrix)):
    for j in range(1, len(dp_matrix[i])):
        if(coins[i] <= j):
            dp_matrix[i][j] = dp_matrix[i-1][j] + dp_matrix[i][j - coins[i]]
        else:
            dp_matrix[i][j] = dp_matrix[i-1][j]

while(T>0):
    N = int(input())
    print(dp_matrix[len(dp_matrix)-1][N]%1000000007)
    T-=1
