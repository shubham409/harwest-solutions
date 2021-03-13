def fun(ls):
    l=['H','Q','9']
    for i in l:
        if(i in ls):
            print('YES')
            return
    print('NO')




# T=int(input())
# for i in range(T):
#     ls= list(map(int,input().split()))
#     fun(ls)
t=input()
fun(t)