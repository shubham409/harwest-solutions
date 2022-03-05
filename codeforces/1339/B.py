def fun(ls,n):
    st = sorted(ls)
    index = 0
    ans =[]
    left = 0
    right = len(st) -1
    while(left<=right):
        if (left!=right):
            ans.append(st[right])
            ans.append(st[left])
            left+=1
            right-=1
        else:
            ans.append(st[right])
            left+=1
            right-=1            
    print(*ans[::-1])

    




T = int(input())
for i in range(T):
    # st=input()
    n=int(input())
    ls= list(map(int, input().split()))
    # lt= list(map(int, input().split()))
    fun(ls,n)

