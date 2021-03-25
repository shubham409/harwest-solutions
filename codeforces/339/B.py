def fun(ls,ms):
    n,k=ms
    i=1
    ans=0
    for v in ls:
        if(v>i):
            ans+=(v-i)
            i=v
        elif v==i:
            continue
        else:
            # v<i
            # go from i to n then 1 again
            ans+=(n-i)+1
            i=1
            ans+=(v-i)
            i=v
    print(ans)

for i in range(1):
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ms)