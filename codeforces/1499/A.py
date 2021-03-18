def fun(ls,lt):
    n,k1,k2=ls
    w,b=lt
    total_box=n*2
    max_white_domino = (k1+k2)//2
    max_black_domino= (total_box-(k1+k2))//2
    if(max_black_domino>=b and max_white_domino>=w):
        print('YES')
    else:
        print('NO')

T = int(input())
for i in range(T):
    ls= list(map(int, input().split()))
    lt= list(map(int, input().split()))
    fun(ls,lt)