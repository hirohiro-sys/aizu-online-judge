s = input()
count = 0
while True:
    text = input()
    if text=="END_OF_TEXT":
        break
    # 小文字と大文字区別しないから全部小文字にする、splitでリストにする
    count += text.lower().split().count(s)
print(count)