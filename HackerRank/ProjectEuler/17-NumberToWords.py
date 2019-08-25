# 17. Number to Words
# Language: Python 3
# Testcases: 6/6


def num_to_word(a,ind_a,p):
    units = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    word = ""
    if(len(str(a))==1):
        if(a!=0):
            word = units[a]
        else:
            word = ""
    elif(len(str(a))==2):
        if(a==0):
            word = ""
        elif(a<20):
            word = teens[a-10]
        else:
            word = tens[int(str(a)[-2])]+" "+units[int(str(a)[-1])]
    elif(len(str(a))==3):
        if(a==0):
            word = ""
        elif(int(str(a)[-2:])<10):
            word = units[a//100]+" Hundred "+units[int(str(a)[-1])]
        elif(int(str(a)[-2:])<20):
            word = units[a//100]+" Hundred "+teens[int(str(a)[-1])]
        else:
             word = units[a//100]+" Hundred "+tens[int(str(a)[-2])]+" "+units[int(str(a)[-1])]
    if(p-ind_a==4 and a!=0):
        word+=" Billion "
    elif(p-ind_a==3 and a!=0):
        word+=" Million "
    elif(p-ind_a==2 and a!=0):
        word+=" Thousand "
    return word

T=int(input())
while(T!=0):
    N=int(input())
    list_parts = []
    if(len(str(N))%3!=0):
        parts=len(str(N))//3+1
    else:
        parts=len(str(N))//3
    if(parts==1):
        list_parts.append(int(str(N)))
    elif(parts==2):
        list_parts.append(int(str(N)[:-3]))
        list_parts.append(int(str(N)[-3:]))
    elif(parts==3):
        list_parts.append(int(str(N)[:-6]))
        list_parts.append(int(str(N)[-6:-3]))
        list_parts.append(int(str(N)[-3:]))
    elif(parts==4):
        list_parts.append(int(str(N)[:-9]))
        list_parts.append(int(str(N)[-9:-6]))
        list_parts.append(int(str(N)[-6:-3]))
        list_parts.append(int(str(N)[-3:]))
    word_string = ""
    count=0
    for i in list_parts:
        word_string+=num_to_word(i,count,parts)
        count+=1
    if(N==0):
        word_string+="Zero"
    elif(N==1000000000000):
        word_string+="One Thousand Billion"
    print(word_string.replace('  ',' '))
    T-=1