def fun(ls,val):
    if(val==1):
        if(ls[0]%2==0):
            print(1)
            print(1)
            return
        print(-1)
        return
    f=ls[0]
    s=ls[1]
    if(f%2==0 or s%2==0):
        if(f%2==0):
            print(1)
            print(1)
            return
        else:
            print(1)
            print(2)
            return
    print(2)
    print(1,2)


    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,val)