# 11. Largest product in a grid
# Language: Python 3
# Testcases: 6/6

T=20
grid = []
while(T!=0):
    line = [int(i) for i in input().strip().split(' ')]
    grid.append(line)
    T-=1
max_prod = 0
# for vertical horizontal and both diagonals
for i in range(0,20):
    for j in range(0,17):
        h_prod=grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if(h_prod>max_prod):
            max_prod=h_prod
for i in range(0,17):
    for j in range(0,20):
        v_prod=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if(v_prod>max_prod):
            max_prod=v_prod
for i in range(0,17):
    for j in range(0,17):
        pd_prod=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if(pd_prod>max_prod):
            max_prod=pd_prod
for i in range(0,17):
    for j in range(0,17):
        apd_prod=grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3]
        if(apd_prod>max_prod):
            max_prod=apd_prod
# for edges
if(max(grid[0][0],grid[0][19],grid[19][0],grid[19][19])>max_prod):
    max_prod=max(grid[0][0],grid[0][19],grid[19][0],grid[19][19])
if(max(grid[1][0]*grid[0][1],grid[0][18]*grid[1][19],grid[18][0]*grid[19][1],grid[19][18]*grid[18][19])>max_prod):
    max_prod=max(grid[1][0]*grid[0][1],grid[0][18]*grid[1][19],grid[18][0]*grid[19][1],grid[19][18]*grid[18][19])
if(max(grid[2][0]*grid[1][1]*grid[0][2],grid[0][17]*grid[1][18]*grid[2][19],grid[17][0]*grid[1][18]*grid[2][19],grid[19][17]*grid[18][18]*grid[17][19])>max_prod):
    max_prod=max(grid[2][0]*grid[1][1]*grid[0][2],grid[0][17]*grid[1][18]*grid[2][19],grid[17][0]*grid[18][1]*grid[19][2],grid[19][17]*grid[18][18]*grid[17][19])
print(max_prod)