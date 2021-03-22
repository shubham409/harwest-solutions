def fun(lt,s):
    st=sorted(lt)
    for strength,bonus in st:
        if(s>strength):
            s+=bonus
        else:
            print('NO')
            return
    print('YES')
S,T = list(map(int, input().split()))
lt=[]
for i in range(T):
    ls= list(map(int, input().split()))
    lt.append(ls)    
fun(lt,S)