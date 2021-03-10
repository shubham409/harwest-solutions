def fun(ls):
    count=0
    for living,space in ls:
        if(space-living >=2):
            count+=1
    print(count)
    


    

T = int(input())
ls= []
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ms= list(map(int, input().split()))
    lt= list(map(int, input().split()))
    ls.append(lt)

fun(ls)