def fun(ls):
    
    even =0
    odd = 0 
    for i in ls:
        if(i%2==0)  :
            even+=1
        else:
            odd+=1
    if(even==odd):
        print('Yes')
    else:
        print('No')




T = int(input())
for i in range(T):
    # n,k= list(map(int, input().split()))
    n= int(input())
    ls= list(map(int, input().split()))
    fun(ls)