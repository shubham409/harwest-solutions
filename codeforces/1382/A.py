def fun(ls,ms):
    st=set(ls)
    for i in ms:
        if i in st:
            print('Yes')
            print(1,i)
            return
    print('No')


        


T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=(input())
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls,ms)