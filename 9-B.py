while True:
    text = input()
    if text == "-":
        break

    n = int(input())
    for i in range(n):
        m = int(input())
        text = text[m:]+text[:m]
    print(text)