#入力
a,b = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(a)]

#行の合計
for i in range(a):
    li[i].append(sum(li[i]))

#列の合計
#配列の縦検索
tmp = [0]*(b+1)
for i in range(b+1):
    for j in range(a):
        tmp[i]+=li[j][i]

#出力
for i in range(a):
    print(*li[i])
print(*tmp)