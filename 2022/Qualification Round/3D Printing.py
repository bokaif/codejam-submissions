def dumb(c1, c2, c3):
    n = 10**6
    c, m, y, k = [min(c1[i], c2[i], c3[i]) for i in range(4)]
    s = c + m + y + k
    if s < n:
        return 'IMPOSSIBLE'
    elif s == n:
        return f'{c} {m} {y} {k}'
    else:
        s = i = 0
        l = [c, m, y, k]
        while s < n:
            s += l[i]
            i += 1
        ll = l[:i] if s == n else l[:i-1] + [n - sum(l[:i - 1])]
        return ' '.join(map(str, ll)) + (4 - len(ll)) * ' 0'

for t in range(int(input())):
    c1, c2, c3 = [[*map(int, input().split())] for i in [1]*3]
    print(f'Case #{t+1}: {dumb(c1, c2, c3)}')