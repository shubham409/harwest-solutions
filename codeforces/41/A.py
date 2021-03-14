def fun(l,s):
    if l==s[::-1]:
        print('YES')
    else:
        print('NO')
    
    

T = (input())
S = (input())
# T = int(input())
# for i in range(T):
#     # var=input()
#     # st=input()
#     # val=int(input())
#     # ms= list(map(int, input().split()))
#     ls= list(map(int, input().split()))
#     fun(ls)
fun(T,S)
