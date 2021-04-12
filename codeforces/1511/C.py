def fun(ls,ms,qs):
    all_color=[None for i in range(51)]
    maxi=0
    for i ,val in enumerate(ls):
        i+=1
        if(all_color[val]==None):
            all_color[val]=i
            maxi=max(maxi,val)    
    ans=[]
    for q in qs:
        index=all_color[q]
        
        print(index,end=" ")
        for current_index in range(51):
            val=all_color[current_index]
            if (val!=None and val<index):
                all_color[current_index]=all_color[current_index]+1
        all_color[q]=1
    print()


T = 1
for i in range(T):
    ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    qs=list(map(int, input().split()))
    fun(ls,ms,qs)