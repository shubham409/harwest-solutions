def fun(lt,k,n):
    
    for i in range(n):
        max_distance=0
        for j in range(n):
            val1=lt[i]
            val2=lt[j]
            max_distance= max(abs(val2[0]-val1[0])+abs(val2[1]-val1[1]),max_distance)
        if(max_distance<=k):
            print(1)
            return
    print(-1)
    
T = int(input())
for _ in range(T):
    n,k= list(map(int, input().split()))
    lt=[]
    for _ in range(n):
        ls= list(map(int, input().split()))
        lt.append(ls)
    fun(lt,k,n)