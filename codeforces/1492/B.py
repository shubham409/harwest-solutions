def fun(ls,var):
    dct={}
    for i,val in enumerate(ls):
        
        dct[val]=i
    st=sorted(ls)
    last_pop_index=var
    ans=[]
    for i in st[::-1]:
        get_index=dct.get(i)
        if(get_index<last_pop_index):
            for j in range(get_index,last_pop_index):
                ans.append(ls[j])
            last_pop_index=get_index
    print(*ans)


T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    v=int(input())
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,v)