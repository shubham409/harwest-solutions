def fun(ls,val):
    rv=ls[::-1]
    ans=[]
    max_so_far=0
    for i in rv:
        max_so_far= max(max_so_far,i)
        if(max_so_far>0):
            ans.append(1)
        else:
            ans.append(0)
        max_so_far-=1
    print(*ans[::-1])

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=int(input())
    # lt= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,val)