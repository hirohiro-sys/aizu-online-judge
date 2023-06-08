import math
a,b,c = map(int,input().split())
rad = math.radians(c)

S = a*b*math.sin(rad)*0.5
H = 2*S/a
C = math.sqrt(a**2+b**2-2*a*b*math.cos(rad))

L = a+b+C

print(S,L,H,sep="\n")