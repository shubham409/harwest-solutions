from collections import Counter

def fun(ls):
    dct=Counter(ls)
    ans=0
    for i in dct.keys():
        ans=max(ans,dct.get(i))
    print(ans)


# T = int(input())
T=1
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    # ls= list(input())
    # qs=list(map(int, input().split()))
    fun(ls)