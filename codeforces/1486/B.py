def fun(a,b,val):
    a=sorted(a)
    b=sorted(b)
    if(val%2!=0):
        print(1)
    else:
        median1=val//2
        median2=median1-1
        x_median1=a[median1]
        x_median2=a[median2]
        y_median1=b[median1]
        y_median2=b[median2]
        x_med=(x_median1- x_median2)+1
        y_med=(y_median1- y_median2)+1
        print(x_med*y_med)

    

    

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    val=int(input())
    X=[]
    Y=[]
    for i in range(val):
    # ms= list(map(int, input().split()))
        x,y= list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    fun(X,Y,val)