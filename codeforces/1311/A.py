def fun(ls):
    a,b=ls
    # can add odd or substract even
    if(a<=b):
        if(a==b):
            print(0)
            return
        if(a%2==0):
            if(b%2==0):
                print(2)
            else:
                print(1)

        else:
            # a is odd
            if(b%2==0):
                print(1)
            else:
                print(2)
    else:
        if(a%2==0):
            if(b%2==0):
                print(1)
            else:
                print(2)

        else:
            # a is odd
            if(b%2==0):
                print(2)
            else:
                print(1)         
    
    


                             

T = int(input())
for _ in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    # ks= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)