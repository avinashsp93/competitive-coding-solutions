# 19. Counting Sundays
# Language: Python 3
# Testcases: 8/8 

T = int(input())
while(T > 0):
    Y1,M1,D1 = [int(i) for i in input().strip().split(' ')]
    Y2,M2,D2 = [int(j) for j in input().strip().split(' ')]


    if(D1 != 1):
        M1+=1

    if(M1 < 3):
        M1+=12
        Y1-=1
    if(M2 < 3):
        M2+=12
        Y2-=1

    # reference day, 1/1/1900 -> 13th month of 1899 for formula
    ref_day = (1 + (13*(13+1)//5) + 99 + 99//4 + 18//4 + 5*18)%7

    # h = (q + 13(m+1)//5 + K + K//4 + J//4 + 5J)mod 7
    
    sunday_count = 0

    for i in range(Y1, Y2+1):
        if(i == Y1):
            monthStart = M1
        else:
            monthStart = 3
        
        if(i == Y2):
            monthEnd = M2
        else:
            monthEnd = 14
        for j in range(monthStart, monthEnd+1):
            # print(j, i)
            q1 = 1
            m1 = j
            K1 = i%100
            J1 = i//100    

            # print((q1 + 13*(m1 + 1)//5 + K1 + K1//4 + J1//4 + 5*J1)%7)
            if((q1 + 13*(m1 + 1)//5 + K1 + K1//4 + J1//4 + 5*J1)%7 == 1):
                # print(1, j, i)
                sunday_count += 1
        
    # inclusion check
    if(1 + 13*(M2 + 1)//5 + (Y2%100) + (Y2%100)//4 + (Y2//100)//4 + 5*(Y2//100)%7 == 1):
        sunday_count+=1
    print(sunday_count)

    T-=1