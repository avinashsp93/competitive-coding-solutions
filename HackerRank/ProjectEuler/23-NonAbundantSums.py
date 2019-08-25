# 23. Non-abundant sums
# Language: Python 3
# Testcases: 2/4
# Reason: Testcases terminating due to timeout

T = int(input())
abundant_nums = []
for i in range(2,10000):
    count = 1
    for j in range(2,i):
        if(i%j==0):
            count+=j
    if(count>i):
        abundant_nums.append(i)
abundant_sums = []
for i in range(0,len(abundant_nums)):
    for j in range(i,len(abundant_nums)):
        abundant_sums.append(abundant_nums[i]+abundant_nums[j])
while(T!=0):
    num = int(input())
    if num in abundant_sums:
        print("YES")
    elif(num>28123):
        print("YES")
    else:
        print("NO")
    T-=1