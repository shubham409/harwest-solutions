def fun(ls):
    mn=min(ls)
    ls[0]=ls[0]-mn
    ls[1]=ls[1]-mn
    rem=max(ls)//2
    print(mn,rem)

ls = list(map(int, input().split()))
fun(ls)