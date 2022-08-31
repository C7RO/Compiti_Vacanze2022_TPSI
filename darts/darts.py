import math
def score(x, y):
    dis= math.sqrt(x**2+y**2)
    if dis > 10:
        return 0
    if dis > 5:
        return 1
    if dis> 1:
        return 5
    else:
        return 10
