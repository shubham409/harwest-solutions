yes='YES'
no='NO'
def fun(ls,n):
    st=sorted(ls)
    st=list(reversed(st))
    if(n==1):
        print(yes)
        return
    prv=st[0]
    for i in st[1:]:
        if(prv-i>1):
            print(no)
            return
        prv=i
    print(yes)

T = int(input())
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    st= list(map(int, input().split()))
    # fun(ls)
    fun(st,val)