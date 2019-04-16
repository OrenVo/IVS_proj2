#!/usr/bin/python


###############################################################################
# @file deus_profiling.c
# @brief Calculation of the standard deviation of numbers from the inputfile.
#
# @author Pavol Szepsi
#
# @version 1.7.0
# @date 15.4.2019
###############################################################################


import sys
import deus_math_lib


##
# @brief Function calculates standard deviation.
#
# @return Standard deviation of numbers from input.
def StandardDeviation():
    sumX = 0
    sumX2 = 0
    N = 0

    for x in sys.stdin:
        x = float(x)
        sumX = deus_math_lib.deus_sum(sumX, x)
        sumX2 = deus_math_lib.deus_sum(sumX2, deus_math_lib.deus_pow(x, 2))
        N = deus_math_lib.deus_sum(N, 1)

    avgX = deus_math_lib.deus_div(sumX, N)
    return deus_math_lib.deus_root(deus_math_lib.deus_mult(deus_math_lib.deus_div(1, deus_math_lib.deus_sub(N, 1)), deus_math_lib.deus_sub(sumX2, deus_math_lib.deus_mult(N, deus_math_lib.deus_pow(avgX, 2)))), 2)

print(StandardDeviation())


###############################################################################
# @}
# End of the deus_profiling.py
###############################################################################
