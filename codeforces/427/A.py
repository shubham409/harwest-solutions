def fun(ls):
    ans =0
    sm=0
    for i in ls:
        if(sm<=0 and i<0):
            ans+=i
        else:
            sm+=i
    print(abs(ans))

n = int(input())
ls = list(map(int, input().split()))
fun(ls)