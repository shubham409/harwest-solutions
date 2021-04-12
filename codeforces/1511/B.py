def fun(ls):
    ans1=[0,
        7,
        49,
        343,
        2401,
        16807,
        117649,
        5764801,
        40353607,
        282475249,
        1977326743
        ]
    ans2=[1,
        5,
        25,
        125,
        3125,
        15625,
        390625,
        1953125,
        48828125,
        244140625,
        1220703125]

    a,b,c=ls
    if(a==1 and b==1 and c==1):
        print(1,1)
        return
    if c==1:
        print(ans1[a],ans2[b])
        return
    else:
        if (a!=b):
            a=a-1
            show1=10**a
            show2=ans1[b-c+1]*(10**(c-1))
            print(show1,show2)
        else:
            l1=a
            ans=[0,
                7,
                49,
                343,
                2401,
                16807,
                117649,
                5764801,
                40353607,
                282475249,
                1977326743
                ]
            if(b-c!=0):
                a=a-1
                show1=10**a
                show2=ans[b-c+1]*(10**(c-1))
                print(show1,show2)
            else:
                a=a-1 
                mn=min(b,c)
                mn=mn-1
                print(10**a,10**mn)


T = int(input())
# T = 0
for i in range(T):
    # var=input()
    # val=int(input())
    # st=input()
    # ms= list(map(int, input().split()))
    ls= list(map(int, input().split()))
    fun(ls)