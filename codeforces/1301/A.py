test = int(input())
for t in range(test):
  a=input()
  b=input()
  c=input()
  for x in range(len(a)):
    if a[x]!=c[x] and b[x]!=c[x]:
      print("NO")
      break
  else:
    print("YES")