def fun(n,ls):

    for i in range(5):
        for j in range(i+1,5):
            prefer_i=0
            prefer_j=0
            both= 0
            for k in range(n):
                val1=ls[k][i]
                val2=ls[k][j]
                if(val1==1 and val2==1):
                    both+=1
                    continue
                if(val1==1):
                    prefer_i+=1
                    continue
                if(val2==1):
                    prefer_j+=1
            if(prefer_j==prefer_i and prefer_i>=(n//2)):
                print('YES')
                return
            maxx= max(prefer_j,prefer_i)
            minn= min(prefer_j,prefer_i)
            extra = maxx-minn
            if(both>=extra):
                both-=extra
                minn+=extra
                if(both%2==0):
                    if((maxx+(both//2))>=(n//2) and (minn +(both//2))>=(n//2)):
                        print('YES')
                        return
    print('NO')
    return


T = int(input())
for _ in range(T):
    n = int(input())
    ls = []
    for _ in range(n):
        lt = list(map(int, input().split()))
        ls.append(lt)
    fun(n,ls)

        







