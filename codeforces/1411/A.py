def fun(st,n):
    cb=')'
    count=0
    for i in st[::-1]:
        if(i==cb):
            count+=1
        else:
            break
    # print(n-count,count)
    if(n-count<count):
        print('Yes')
    else:
        print('No')

    

T = int(input())
for i in range(T):
    # var=input()
    val=int(input())
    st=input()
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    # fun(ls)
    fun(st,val)