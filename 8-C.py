#sys.stdin.readで複数行入力
import sys
s = sys.stdin.read()
#大文字も判定に含めるから小文字にする
s = s.lower()

for i in range(97,123):
    print(f"{chr(i)} : {s.count(chr(i))}")