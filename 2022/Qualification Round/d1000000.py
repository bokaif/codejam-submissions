def dumb(l):
    n = 1
    for i in l:
        n += 1 if i >= n else 0
    return n - 1

for t in range(int(input())):
    input()
    l = sorted(map(int, input().split()))
    print(f'Case #{t+1}: {dumb(l)}')