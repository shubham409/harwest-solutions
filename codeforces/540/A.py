def fun(ls,ms):
    ans=0
    for i,j in zip(ls,ms):
        # +1 for  9 to 0
        mn=min(abs(i-j),( abs(i-9) + abs(j-0) +1) ,( abs(i-0) + abs(j-9) +1) )
        ans+=(mn)
    print(ans)


for i in range(1):
    val=int(input())
    ms= list(map(int, list(input())))
    ls= list(map(int, list(input())))
    fun(ls,ms)