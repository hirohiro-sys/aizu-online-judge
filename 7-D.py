#問題文通り実装する 線形代数計算
n,m,l = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(n)]
B = [list(map(int,input().split())) for _ in range(m)]
for i in range(n):
    C = []
    for j in range(l):
        tmp = 0
        for k in range(m):
            tmp+=A[i][k]*B[k][j]
        C.append(tmp)
    print(*C)