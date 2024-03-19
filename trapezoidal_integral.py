from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------
N = 100
a = 0
b = 0.5 *(math.pi)
h =  (b - a) / N
c = 1
S = 0
for c in range(N):
    c +=1
    S += h/2 * (sin(a+(c-1)*h) + sin(a+c*h))
    
print(S)