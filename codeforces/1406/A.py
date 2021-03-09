def fun(ls,n):
    count=[0 for i in range(101)]
    for i in ls:
        count[i]+=1
    first_nonrepating=None
    first_absent=None
    for i,val in enumerate(count):
        if (val<=1 and first_nonrepating==None):
            first_nonrepating=i
        if(val==0 and first_absent==None):
            first_absent=i
    # if(first_absent==0 and first_nonrepating ==1):
    #     print(0)
    #     return
    # if(first_nonrepating==None):
    #     print(first_absent)
    #     return

    print(first_absent+first_nonrepating)



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