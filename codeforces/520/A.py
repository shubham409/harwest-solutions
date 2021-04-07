def fun(ls,n):
    st='qwertyuiopasdfghjklzxcvbnm'
    st=set(list(st))
    ls=ls.lower()
    ls=set(ls)
    if(st==ls):
        print("YES")
    else:
        print('NO')


    
# T = int(input())
for _ in range(1):
    # var=input()
    # st=input()
    # n=int(input())
    # a=input()
    # b=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    n=int(input())
    st=input()
    fun(st,n)