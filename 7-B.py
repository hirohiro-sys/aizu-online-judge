while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    count = 0
    for i in range(1,a+1):
        for j in range(i+1,a+1):
            for k in range(j+1,a+1):
                if i+j+k==b:
                    count += 1
    print(count)