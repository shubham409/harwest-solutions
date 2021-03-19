from collections import Counter 
from math import ceil,floor,sqrt,gcd
def fun(ls):
    lt= sorted(ls)
    dct={}
    ctr=Counter(ls)
    j=1
    for i in ls:
        dct[i]=j
        j+=1
    for i in lt:
        if(ctr.get(i)==1):
            print(dct.get(i))
            return
    print(-1)

    
        


    


T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=int(input())
    # st=input()
    ls= list(map(int, input().split()))    
    fun(ls)