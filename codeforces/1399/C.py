def fun(ls,n):
    max_team = -10**9

    org_mapper = [0 for i in range(2*n+1)]
    for i in range(0,n):
        val = ls [i]
        org_mapper[val]+=1

    for team_weight in range(1,1+(2*n)):
        mapper = org_mapper.copy()
        current_team = 0
        for individual_weight , count in enumerate(mapper):
            # when this value is half of the sum 
            if individual_weight==0 :
                # no team with zero members can be formed 
                continue
            if (individual_weight*2 == team_weight):
                current_team+= (count//2)

            else:
                if(individual_weight>=team_weight):
                    continue
                else:
                    current_count=count
                    current_weight=individual_weight

                    required_weight=team_weight -  individual_weight
                    left_count= mapper[required_weight]

                    mn = min(count,left_count)
                    mapper[individual_weight]-= mn 
                    mapper[required_weight]-= mn

                    current_team+=mn 
        max_team= max(max_team , current_team)
    print(max_team)





T = int(input())
for i in range(T):
    # st=input()
    n=int(input())
    ls= list(map(int, input().split()))
    # lt= list(map(int, input().split()))
    fun(ls,n)



