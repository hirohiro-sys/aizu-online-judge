#後ろの反復文が内側のループ
all = [(i,j) for i in ["S","H","C","D"] for j in range(1,14)]
hold = []
n = int(input())
for i in range(n):
    a,b = input().split()
    hold.append((a,int(b)))
for i in all:
    if i not in hold:
        print(*i)