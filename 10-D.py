n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
#問題文よりpが1~3のミンコフスキー距離と無限の時のミンコフスキー距離の4つを出力する 
for p in range(1,4):
    print("{0:.6f}".format(sum([abs(a-b)**p for a,b in zip(x,y)])**(1/p)))
print("{0:.6f}".format(max([abs(a-b) for a,b in zip(x,y)])))