def fun(ls):
    prv=ls[0]
    count=1
    for i in ls[1:]:
        if(i!=prv):
            prv=i
            count+=1
    print(count)


T = int(input())
ls=[]
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    st=input()
    ls.append(st)
    # ls= list(map(int, input().split()))    
fun(ls)