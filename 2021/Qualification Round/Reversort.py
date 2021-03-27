for t in range(int(input())):
  l=int(input())
  L=input().split()
  x=0
  for i in range(l-1):
    j=d=i
    for c in range(d,l):
      if int(L[c])<int(L[j]):j=c
    A=i
    B=j
    while A<B:
      m=L[A]
      L[A]=L[B]
      L[B]=m
      A+=1
      B-=1
    x+=j-i+1
  print(f"Case #{t+1}: {x}")
