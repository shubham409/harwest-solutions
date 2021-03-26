def fun(ls,ms):
    n,k=ms
    min_index= None
    star='*'
    ans=1
    for i,val in enumerate(ls):
        if val==star:
            min_index=i
            break
    while(True):
        j=min(n-1,i+k)
        while(i<j and ls[j]=='.'):
            j-=1
        if(i==j):
            break
        i=j
        ans+=1
    print(ans)

T = int(input())
for i in range(T):
    ms= list(map(int, input().split()))
    st=input()
    fun(st,ms)