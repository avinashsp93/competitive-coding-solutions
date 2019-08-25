# 14. Longest Collatz Sequence
# Language: Python 2
# Testcases: 5/13
# Reason: Testcases terminating due to timeout

T = int(input())
while(T!=0):
    max_list = []
    N = int(input())
    col_dic = {}
    for i in range(1,N+1):
        count = 1
        n=i
        while(n!=1):
            if(n%2==0):
                n/=2
            else:
                n=3*n+1
            count+=1
        if(i!=1):
            if(count>=max(col_dic.values())):
                col_dic[i]=count
        else:
            col_dic[i]=count
    max_value=max(col_dic.values())
    for a,b in col_dic.items():
        if(b==max_value):
            max_list.append(a)
    print(max(max_list))
    T-=1