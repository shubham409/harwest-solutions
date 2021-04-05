def fun(a,b,n):
    a+='0'
    b+='0'
    count=0
    for i in range(n):
        val=a[i]
        if(val=='1'):
            count+=1
        else:
            count-=1
        if((a[i]==b[i])!=(a[i+1]==b[i+1]) and count!=0):
            print('no')
            return
    print('yes')
            
        

    
    
T = int(input())
for _ in range(T):
    n=int(input())
    a=input()
    b=input()
    fun(a,b,n)