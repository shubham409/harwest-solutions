from collections import Counter
from math import ceil 
def fun(ls,n,k):
    for i in range(n):
        ls[i]=(ls[i]%k)
    ans=0
    dct=Counter(ls)
    # print(dct)
    for i in range((k//2)+1):
            val1= dct.get(i)
            val2= dct.get(k-i)
            if(val1 != None and val2!= None):
                if(k%2!=0):
                    if(val1>val2):
                        ans+=1 # for min(val1,val2)
                        ans+= (val1 - val2 -1)
                        dct[i]=None
                        dct[k-i]=None
                    elif val1==val2:
                        ans+=1 # for min(val1,val2)
                        dct[i]=None
                        dct[k-i]=None                         
                    else:
                        ans+=1 # for min(val1,val2)
                        ans+= (val2 - val1 -1)
                        dct[i]=None
                        dct[k-i]=None
                else:   
                    if(i==(k//2)):
                        dct[i]=None
                        ans+=1 #all n//2 is present in it 

                    else:
                        if(val1>val2):
                            ans+=1 # for min(val1,val2)
                            ans+= (val1 - val2 -1)
                            dct[i]=None
                            dct[k-i]=None
                        elif val1==val2:
                            ans+=1 # for min(val1,val2)
                            dct[i]=None
                            dct[k-i]=None                                                        
                        else:
                            ans+=1 # for min(val1,val2)
                            ans+= (val2 - val1 -1)
                            dct[i]=None
                            dct[k-i]=None                          

            if(val1 == None and val2!= None):
                ans+=val2
                dct[k-i]=None  


            if(val1 != None and val2== None):
                if(i==0):
                    ans+=1
                    dct[i]=None
                else:
                    ans+=val1
                    dct[i]=None


    print(ans)                         
            

T = int(input())
for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    n,k= list(map(int, input().split()))
    ls = list(map(int, input().split()))
    fun(ls,n,k)
    # fun(st,var)

