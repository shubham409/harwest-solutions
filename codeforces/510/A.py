def fun(n):
    r,c=n
    same='#'*c
    left='#'+'.'*(c-1)
    right='.'*(c-1)+'#'
    bl=True
    for i in range(r):
        if(i%2==0):
            print(same)
        else:
            if(bl):
                print(right)
                bl=False
            else:
                print(left)
                bl=True


ls= list(map(int, input().split()))
fun(ls)