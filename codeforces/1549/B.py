def fun(st,ts):
    # print(st,ts)
    count=0
    for i in range(n):
        enemy = st[i]
        me = ts[i]
        
        if(i==0):
            if(me==1):
                if(enemy==0):
                    st[i]=-1
                    count+=1
                else:
                    if(st[i+1]==1):
                        st[i+1]=-1
                        count+=1
            continue
        if(i==n-1):
            if(me==1):
                if(enemy==0):
                    st[i]=-1
                    count+=1
                else:
                    if(st[i-1]==1):
                        st[i-1]=-1
                        count+=1
            continue
        else:
            if(me==1):
                if(enemy==0):
                    st[i]=-1
                    count+=1
                else:
                    if(st[i-1]==1):
                        st[i-1]=-1
                        count+=1
                    else:
                        if(st[i+1]==1):
                            st[i+1]=-1
                            count+=1                        
    print(count)
    # print(st,ts)
T = int(input())
# T=1
for i in range(T):
    n=int(input())
    # ks= list(map(int, input().split()))  
    # ls= list(map(int, input().split()))   
    # print(ls) 
    st=list(input())
    ts=list(input())
    st= list(map(int, st))  
    ts= list(map(int, ts))  

    # ts=input()
    # ls= list(map(int, input().split()))
    fun(st,ts)
    