from string import ascii_lowercase 
def fun(st,ls,querry):
    n,q=ls
    dct={}
    j=1
    ans=''
    temp= ascii_lowercase
    # print(temp)
    for i in temp:
        if(i not in dct):
            dct[i]=j
            j+=1
    prefix_ar=[0 for i in range(n)]
    j=0
    total_length=0
    for i in st:
        get_count=dct.get(i)
        ans+=i*get_count
        prefix_ar[j]=get_count
        total_length+=get_count
        j+=1
    # print(prefix_ar)
    prefix_sum=[0 for i in range(n)]
    for i in range(n):
        if(i==0):
            prefix_sum[i]=prefix_ar[i]
        else:
            prefix_sum[i]=prefix_ar[i]+prefix_sum[i-1]
    # print(prefix_sum)
    for i,j in querry:
        if(i!=1):
            print(prefix_sum[j-1]-prefix_sum[i-2])
        else:
            print(prefix_sum[j-1])


T=1
for i in range(T):
    ls= list(map(int, input().split()))    
    st=input()
    querry=[]
    for k in range(ls[1]):
        ks= list(map(int, input().split()))
        querry.append(ks)
    fun(st,ls,querry)