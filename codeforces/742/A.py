def fun(ls):
    if(ls==0):
        print(1)
        return
    dct={0:6,1:8,2:4,3:2}
    print(dct.get(ls%4))


# T = int(input())
T=1
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(val)