def dumb(r, c):
    br = '+'+'-+'*c
    pr = '|'+'.|'*c
    for i in range(r+r+1):
        if i&1:
            print('..'+pr[2:] if i==1 else pr)
        else:
            print('..'+br[2:] if i==0 else br)
    

for t in range(int(input())):
    r, c = map(int, input().split())
    dumb(r, c)