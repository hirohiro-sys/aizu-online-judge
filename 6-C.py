#3次元配列入力
li = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
for i in range(n):
    b,f,r,v = map(int,input().split())
    li[b-1][f-1][r-1]+=v

#出力
for i in range(4):
    for j in li[i]:
        print("",*j)
    if i!=3:
        print("####################") 