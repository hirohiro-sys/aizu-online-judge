n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
li2 = [int(input()) for _ in range(m)]

for i in range(n):
    result = 0
    for j in range(m):
        result+=li[i][j]*li2[j]
    print(result)