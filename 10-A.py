# hypotでユークリッド距離を求める　ユークリッド距離とは二点の直線距離のこと
import math
x1,y1,x2,y2 = map(float,input().split())
print(math.hypot(x2-x1, y2-y1))