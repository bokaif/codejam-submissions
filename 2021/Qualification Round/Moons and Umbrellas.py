#couldn't pass hidden test set
for t in range(int(input())):
  a,b,c=input().split();x=0;a=int(a);b=int(b);s='0'
  for j in range(len(c)):
    if s=="C" and c[j]=="J":x+=a
    if s=="J" and c[j]=="C":x+=b
    if c[j]!="?":s=c[j]
  print(f'Case #{t+1}: {x}')
