#標準偏差の公式通りに実装
while True:
    n = int(input())
    if n == 0:
        break
    score = list(map(int, input().split()))
    mean = sum(score)/n
    var_sum = 0
    for i in range(n):
        var_sum += (score[i]-mean)**2
    print((var_sum/n)**0.5)