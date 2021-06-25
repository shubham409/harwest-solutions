def fun(n):

    ls=[i for i in range(1,n+1)]
    # print(ls)
    for i in range(n):
        if( i%2!=0):
            now = ls[i]
            prv = ls[i-1]
            ls[i]=prv
            ls[i-1]=now
    if(n%2!=0):
        ls[-1],ls[-2]=ls[-2],ls[-1]
    print(*ls)

    
T = int(input())
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    # fun(ls)
    # v=(int(input()))
    fun(val)