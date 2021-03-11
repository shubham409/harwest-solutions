def fun(val):
    ls=[]
    for i in range(1,10):
        var= str(i)
        ls.append(var)
        ls.append(var*2)
        ls.append(var*3)
        ls.append(var*4)
    count=0
    str_val= str(val)
    for i in ls:
        count+=len(i)
        if(i==str_val):
            print(count)
            return 

    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=int(input())
    # ms= list(map(int, input().split()))
    # ls= list(map(int, input().split()))
    fun(val)
