def fun(n):
    if(n%2==0):
        print(n//2)
        for i in range(n//2):
            print(2,end=' ')
        print()
    else:
        print(((n-3)//2)+1)
        for i in range((n-3)//2):
            print(2,end=' ')
        print(3)

v=(int(input()))
fun(v)