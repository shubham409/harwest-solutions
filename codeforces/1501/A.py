from math import ceil,floor,sqrt
def fun(ls,d):
    prv=0
    original=ls.copy()
    time_to_reach=[]
    for time,delay in zip(ls,d):
        arrival=time[0]
        departure=time[1]
        temp= arrival-prv+delay
        time_to_reach.append(temp)
        prv=departure
    # time to satisfy condition 
    # >=departure and at least ceil([(departure - arrival)/2])
    late_departure=0
    i=0
    ans=[]
    for time,delay in zip(ls,time_to_reach):
        temp=late_departure+delay
        current=ls[i]
        ans.append(temp)
        # condition to set new late deparure
        original_current= original[i]
        start = original_current[0]
        end = original_current[1]
        val=ceil((end-start)/2)
        if(temp+val<=end):
            late_departure=end
        else:
            late_departure=temp+val
        i+=1
    print(ans[-1])
  
T = int(input())
for i in range(T):
    # n = list(map(int, input().split()))
    ls=[]
    n = int(input())
    for i in range(n):
        lt = list(map(int, input().split()))
        ls.append(lt)
    delay = list(map(int, input().split()))
    fun(ls,delay)



