#nまでの整数が3で割り切れるか3が含まれていたら出力する
n = int(input())
for i in range(1,n+1):
    if i%3==0 or "3" in str(i):
        print(i,end=" ") 