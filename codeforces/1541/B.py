def fun(n,st):
    count=0
    pair=[[st[i],i+1] for i in range(n)]
    pair = sorted(pair)
    for i in range(n):
        first=pair[i]
        for j in range(i+1,n):
            second=pair[j]
            if(first[0]*second[0]== first[1]+second[1]):
                count+=1
            if(first[0]*second[0] >2*n ):
                break
    print(count)





    
T = int(input())
for i in range(T):
    # var=input()
    val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    st= list(map(int, input().split()))
    # fun(ls)
    # v=(int(input()))
    fun(val,st)