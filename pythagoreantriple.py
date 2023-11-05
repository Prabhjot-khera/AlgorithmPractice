from math import *

def triple():
    for a in range(1,100):
        for b in range(1,100):
            c=a**2+b**2
            if sqrt(c).is_integer():
                print('a is',a,'b is',b,'which gives a c of',sqrt(c))
triple()


