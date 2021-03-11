from math import ceil,floor,sqrt
def fun(d,m):
    sd=sorted(d)
    sm=sorted(m)
    ans=0
    for i,j in zip(sd,sm):
        ans+= (sqrt((pow(i,2))+(pow(j,2))))
    
    ans2=(0)
    for i,j in zip(sd,sm[::-1]):
        ans2+=(sqrt((pow(i,2))+(pow(j,2))))
    print(min(ans,ans2))

T = int(input())

for i in range(T):
    # var=input()
    # st=input()
    # val=int(input())
    diamond=[]
    miner=[]
    for _ in range(2*int(input())):
        x,y= list(map(int, input().split()))
        if(x==0):
            miner.append(abs(y))
        else:
            diamond.append(abs(x))
    # st=input()
    fun(diamond , miner)
    
