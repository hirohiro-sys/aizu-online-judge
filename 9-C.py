n = int(input())
A_score = 0
B_score = 0
for i in range(n):
    a,b = input().split()
    if a>b:
        A_score+=3
    elif a<b:
        B_score+=3
    else:
        A_score+=1
        B_score+=1
print(A_score,B_score)