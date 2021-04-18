from math import ceil ,floor
def fun(ls):
    a,b,c,d=ls
    total=sum(ls)
    if(ceil(total/3)!=floor(total/3)):
        print('NO')
    else:
        avg=total//3
        if(avg-a>=0 and avg-b>=0 and avg-c>=0):
            print('Yes')
        else:
            print('No')

                             

T = int(input())
for _ in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)