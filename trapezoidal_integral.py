from math import sin
import math

def trape(f,N = 100,a = 0,b = 1):
    h =  (b - a) / N
    c = 1
    S = 0
    for c in range(N):
        c +=1
        S += h/2 * (f(a+(c-1)*h) + f(a+c*h))
    return S

def toiichi(x):
    x = sin(x)
    return x
def toini(x):
    x = 4/(1+x**2)
    return x
def toisan(x):
    x = (math.pi **0.5) * (math.e**(-x**2))
    return x
print (trape(toiichi,50,0,math.pi * 0.5))
print (trape(toini,100,0,1))
print (trape(toisan,1000,-100,100))
