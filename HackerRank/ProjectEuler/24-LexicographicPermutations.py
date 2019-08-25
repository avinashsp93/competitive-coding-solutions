# 24. Lexicographic Permutations
# Language: Python 3
# Testcases: 10/10

T = int(input())

lex_string = "abcdefghijklm"


def factoradic_number(n):
    fact_num = [];
    counter = 1
    while(n!=0):
        fact_num.append(str(n%counter))
        n//=counter
        counter+=1

    if(len(lex_string)+1 - counter != 0):
        return ['0'] * (len(lex_string)+1 - counter) + fact_num[::-1]
    return fact_num[::-1]


while(T>0):
    N = int(input())
    fact_num = factoradic_number(N-1)
    output = []
    lex_list = [i for i in lex_string]
    for i in fact_num:
        output.append(lex_list[int(i)])
        lex_list.remove(lex_list[int(i)])
    print(''.join(output))
    T-=1