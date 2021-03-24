def fun(ls):
    ls=sorted(ls)
    apb,apc,bpc,sm=ls
    print(sm-apb,sm-apc,sm-bpc)

ls = list(map(int, input().split()))
fun(ls)