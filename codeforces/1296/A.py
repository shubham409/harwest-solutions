def fun(ls,n):
    count_even=0
    count_odd=0
    for i in ls:
        if(i%2==0):
            count_even+=1
        else:
            count_odd+=1
    if(n==count_even):
        print('NO')
        return
    if(n==count_odd):
        if(n%2!=0):
            print('YES')
            return

        else:
            print('NO')
    else:
        print('YES')
    

T = int(input())
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # fun(ls)
    # v=(int(input()))
    fun(ls,val)