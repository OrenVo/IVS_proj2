#!/usr/bin/python
# -*- coding: utf-8 -*-


###############################################################################
# @file deus_math_lib.py
# @brief  Library of math functions for the Holy calculator.
#
# @authors Roman Fulla
# @authors Vojtěch Ulej
#
# @version 0.3.2
# @date 14.4.2019
###############################################################################


import math
from random import randint


###############################################################################
# @defgroup BASIC Basic Operations
# @brief Most common math operations.
# @{
###############################################################################


##
# @brief Function adds 2 numbers.
#
# @param a First addend.
# @param b Second addend.
#
# @return The sum of both parameters.
def deus_sum(a, b):
    return a + b


##
# @brief Function subtracts b from a.
#
# @param a Minuend.
# @param b Subtrahend.
#
# @return The difference of both parameters.
def deus_sub(a, b):
    return a - b


##
# @brief Function multiplies 2 numbers.
#
# @param a First factor.
# @param b Second factor.
#
# @return The product of both parameters.
def deus_mult(a, b):
    return a * b


##
# @brief Function divides a by b.
#
# @param a Dividend.
# @param b Divisor.
#
# @return The result of the division of parameters.
# @return NaN (Not a number) if division by zero is attempted.
def deus_div(a, b):
    if b == 0:
        return math.nan
    return a / b


###############################################################################
# @}
#
# @defgroup ADVANCED Advanced Operations
# @brief Less common math operations.
# @{
###############################################################################


##
# @brief Function calculates the a to the power of b.
#
# @param a Base.
# @param b Exponent.
#
# @return a to the power of b (a^b).
def deus_pow(a, b):
    if b == 0:
        return 1
    if a == 0:
        return 0
    return a ** b


##
# @brief Function calculates the bth root of a.
#
# @param a Base.
# @param b Degree.
#
# @return bth root of a.
# @return NaN (Not a number) if the result can't be calculated.
def deus_root(a, b):
    if b == 0:
        return math.nan
    if a == 0 and b > 0:
        return 0
    if a == 0 and b < 0:
        return math.nan
    if a < 0 and (b % 2) == 0:
        return math.nan
    try:
        res = math.pow(a, 1.0/b)
    except ValueError:
        try:
            res = math.pow(abs(a), 1.0/b)
            res = round(res, 10)
            return -res
        except:
            return math.nan
    else:
        return round(res, 10)


##
# @brief Function recursively calculates factorial.
# @details Raises an exception if the fac isn't positve integer.
#
# @param fac Positve integer from which the factorial will be calculated.
#
# @return The product of all positive integers less than or equal to fac(fac!).
def deus_fact_rec(fac):
    if not isinstance(fac, int):
        raise ValueError("Factorial must be integer!")
    if fac < 0:
        raise ValueError("Factorial must be positive value!")
    if fac in (0, 1):
        return 1
    return fac*deus_fact_rec(fac - 1)


##
# @brief Function iteratively calculates factorial.
# @details Raises an exception if the fac isn't positve integer.
#
# @param fac Positve integer from which the factorial will be calculated.
#
# @return The product of all positive integers less than or equal to fac(fac!).
def deus_fact_ite(fac):
    if not isinstance(fac, int):
        raise ValueError("Factorial must be integer!")
    if fac < 0:
        raise ValueError("Factorial must be positive value!")
    if fac == 0:
        return 1
    res = 1
    for x_var in range(1, fac + 1):
        res *= x_var
    return res


##
# @brief Function calculates the logarithm of a to base b.
#
# @param a Positve real number.
# @param b Base, positve real number (except 1).
#
# @return The logarithm of a to base b.
# @return NaN (Not a number) if the result can't be calculated.
def deus_log(a, b):
    try:
        if b == math.e:
            res = math.log(a)
        else:
            res = math.log(a, b)
    except:
        return math.nan
    else:
        return res


###############################################################################
# @}
#
# @defgroup ADJUSTMENTS Number Adjustments
# @brief Simple number adjusting operations.
# @{
###############################################################################


##
# @brief Function calculates abs absolute value.
#
# @param abs Real number.
#
# @return The absolute value of the parameter.
def deus_abs(abs):
    if abs < 0:
        return -abs
    return abs


##
# @brief Function calculates val percentage.
#
# @param val Real number.
#
# @return The percentage value of the parameter.
def deus_percent(val):
    return val / 100


# @brief Function calculates val promille.
#
# @param val Real number.
#
# @return The promille value of the parameter.
def deus_promille(val):
    return val / 1000


###############################################################################
# @}
#
# @defgroup CONSTATNTS Constants
# @brief Operations returning constant value.
#
# @details deus_rnd() returns variable.
#
# @{
###############################################################################


##
# @brief Function returns zero.
#
# @return 0.
def deus_clear():
    return 0


##
# @brief Function returns Euler's number.
#
# @return e (=~ 2.71828182846).
def deus_e():
    return math.e


##
# @brief Function returns Pi.
#
# @return Pi (=~ 3.14159265359).
def deus_pi():
    return math.pi


##
# @brief Function returns random value.
#
# @return Pseudorandom number.
def deus_rnd():
    return randint(-666, 1000)


##
# Super secret hidden function,
# which returns the answer to life,
# the universe and everything!
deus_vult():
    return 42


###############################################################################
# @}
# End of the deus_math_lib.py
###############################################################################
