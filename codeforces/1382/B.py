t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  for i in range(n):
    if a[i]>=2:
      break
  if i%2==0:
    print("First")
  else:
    print("Second")