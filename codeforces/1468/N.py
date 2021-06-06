for _ in range(int(input())):
    c1,c2,c3=map(int,input().split())
    a1,a2,a3,a4,a5=map(int,input().split())
    if a1>c1 or a2>c2 or a3>c3:
        print("NO")
    else:
        c1=c1-a1
        c2=c2-a2
        c3=c3-a3
        k=a4-min(c1,a4)
        l=a5-min(c2,a5)
        if k+l<=c3:
            print("YES")
        else:
            print("NO")    
