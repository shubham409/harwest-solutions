yes="Yes"
no="No"
def fun(ls,lt,k):
    a=sorted(ls)
    b=sorted(lt)
    for i,j in zip(a,b[::-1]):
        if(i+j>k):
            print(no)
            return
    print(yes)

    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # v=int(input())
    n,k= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    lt= list(map(int, input().split()))
    fun(ls,lt,k)
    if(i!=T-1):
        v=input()