while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    elif a>b:
        print(b,a)
    elif a<b:
        print(a,b)
    else:
        print(a,b)