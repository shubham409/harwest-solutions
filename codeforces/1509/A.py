def fun(ls):
    evn=[]
    odd=[]
    for i in ls:
        if(i%2!=0):
            odd.append(i)
        else:
            evn.append(i)
    print(*(odd+evn))

T = int(input())
for i in range(T):
    val=int(input())
    ls= list(map(int, input().split()))
    fun(ls)