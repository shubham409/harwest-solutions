for _ in range(0,int(input())):
  a=int(input())
  b=list(map(int,input().split()))
  t=0
  for i in b:
    t=max(0,t+i)
  print(t)