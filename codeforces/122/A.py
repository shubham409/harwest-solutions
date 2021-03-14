def fun(ls):
    st={'4','7'}
    s4={'4'}
    s7={'7'}
    for i in range(1,ls+1):
        temp=set(list(str(i)))
        if(temp==st or temp==s4 or temp==s7):
            if(ls%i==0):
                print('YES')
                return
    print('NO')
    

T = int(input())
# for i in range(T):
#     # var=input()
#     # st=input()
#     # val=int(input())
#     # ms= list(map(int, input().split()))
#     ls= list(map(int, input().split()))
#     fun(ls)
fun(T)