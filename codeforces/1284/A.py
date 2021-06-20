n,m=map(int,input().split())
s1=input().split()
s2=input().split()
for _ in range(int(input())):
    a=int(input())
    print(s1[a%n-1]+s2[a%m-1])
