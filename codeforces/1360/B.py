def fun(ls):
    st=sorted(ls)
    mn=st[-1]
    prv=st[0]
    for i in st[1:]:
        mn=min(i-prv,mn)
        prv=i
    print(mn)
    

T = int(input())
for i in range(T):
    val=(input())
    ls= list(map(int, input().split()))
    fun(ls)