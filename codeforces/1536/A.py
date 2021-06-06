def fun(ls,n):
    st=sorted(ls)
    if(st[0]<0):
        print('NO')
        return
    else:
        print('YES')
        ans=list(range(101))
        print(101)
        print(*ans)

T = int(input())
for i in range(T):
    n=int(input())
    ls= list(map(int, input().split()))
    fun(ls,n)