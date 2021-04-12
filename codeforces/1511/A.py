def fun(ls):
    type1=0
    type3=0
    type2=0
    for i in ls:
        if (i ==1):
            type1+=1
        if (i ==2):
            type2+=1
        if (i ==3):
            type3+=1
    print(type1+type3)
 

T = int(input())
for i in range(T):
    val=int(input())
    ls= list(map(int, input().split()))
    fun(ls)