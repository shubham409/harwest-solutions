def fun(ls):
    n,a,b=ls
    st=set()
    now=0
    i=0

    if(a==1):
        if((n-1)%b==0):
            print('Yes')
            return
        print('No')
        return
    while(n>now):
        now=a**i
        st.add(now)
        i+=1
    for i in st:
        if(n-i)>=0:
            if((n-i )%b==0 ):
                print('Yes')
                return
    print('No')

        






T = int(input())
# T=1
for i in range(T):
    # n=int(input())
    # ks= list(map(int, input().split()))  
    ls= list(map(int, input().split()))   
    # print(ls) 
    # st=input()
    # ts=input()
    # ls= list(map(int, input().split()))
    fun(ls)