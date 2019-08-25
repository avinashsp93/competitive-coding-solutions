# 30. Digit Nth Powers
# Language: Python 3
# Testcases: 4/4

def split(word): 
    return [char for char in word] 

n = int(input())

main_sum = 0

for j in range(2,600000):
    total=0
    for i in split(str(j)):
        total+=int(i)**n
    if(total == j):
        main_sum+=j
print(main_sum)
