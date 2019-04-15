#!/usr/bin/python

import sys
import deus_math_lib

def StandardDeviation():
    sumX = 0
    sumX2 = 0
    N = 0

    for x in sys.stdin:
        x = float(x)
        sumX += x
        sumX2 += x**2
        N += 1

    avgX = sumX / N
    return deus_math_lib.deus_root((1 / (N - 1) * (sumX2 - (N * deus_math_lib.deus_pow(avgX, 2)))), 2)

print(StandardDeviation())
