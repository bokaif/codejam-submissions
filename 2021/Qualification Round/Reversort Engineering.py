#MLE in 2nd test set

from itertools import permutations

def rev(l, L):
    x1=0
    for i in range(l-1):
        j=d=i
        for c in range(d,l):
            if int(L[c])<int(L[j]): j=c
        A=i
        B=j
        while A<B:
            m=L[A]
            L[A]=L[B]
            L[B]=m
            A+=1
            B-=1
        x1+=j-i+1
    return x1


for i in range(int(input())):
    n, c = map(int, input().split())
    x = list(range(1,n+1))
    x2 = [str(i) for i in x]
    y = [list(p) for p in permutations(x)]
    y2 = [list(p) for p in permutations(x2)]
    z = f'Case #{i+1}: IMPOSSIBLE'

    for j in range(len(y)):
        q = rev(n, y[j])
        if q == c:
            z = f'Case #{i+1}: {" ".join(y2[j])}'
            break
    print(z)
