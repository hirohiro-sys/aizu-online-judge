#円の面積=円周率*半径**2
#円周=2*円周率*半径
import math
radius = float(input())
print("{:.5f}".format(math.pi*radius**2),"{:.5f}".format(2*math.pi*radius))