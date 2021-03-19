def fun(val,ls,lt):
    s=ls[1:]
    t=lt[1:]
    f=s+t
    fs=set(f)
    fb=True
    for i in range(1,val+1):
        if i in fs:
            fb= fb and True
        else:
            fb=fb and False
    if(fb):
        print('I become the guy.')
        return
    print('Oh, my keyboard!')


# T = int(input())
for i in range(1):
    # var=input()
    # st=input()
    val=int(input())
    # st=input()
    lt= list(map(int, input().split()))    
    ls= list(map(int, input().split()))    
    fun(val,ls,lt)