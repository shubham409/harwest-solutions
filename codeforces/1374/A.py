def fun(ls):
    x,y,n=ls
    mod_value = n%x 
    if (mod_value==y):
        print(n)
        return
    if(mod_value>y):
        print(n-(mod_value-y))
        return
    else:
        print(n-(mod_value)-abs(y-x))


T = int(input())
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(ls)