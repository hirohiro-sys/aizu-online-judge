#スライスで解く
s = input()
n = int(input())
for i in range(n):
    order = input().split()
    a,b = map(int, order[1:3])
    if order[0]=="print":
        print(s[a:b+1])
    elif order[0]=="replace":
        s = s[:a] + order[3] + s[b+1:]
    else:
        tmp = s[a:b+1]
        s = s[:a] + tmp[::-1] + s[b+1:]