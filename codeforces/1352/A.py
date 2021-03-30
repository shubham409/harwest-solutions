for _ in range(int(input())):
  A = {a + '0'*i for i, a in enumerate(input()[::-1]) if a != '0'}
  print(len(A))
  print(*A)