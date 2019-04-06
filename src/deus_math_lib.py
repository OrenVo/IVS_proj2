#!/usr/bin/python
# -*- coding: utf-8 -*-
"""docstring for .deus_math_lib"""

##
# @brief Function adds 2 numbers.
#
# @param a First addend.
# @param b Second addend.
#
# @return The sum of both parameters.
def deus_sum(a, b):
    """docstring for function deus_sum"""
    return a + b

##
# @brief Function subtracts b from a.
#
# @param a Minuend.
# @param b Subtrahend.
#
# @return The difference of both parameters.
def deus_sub(a, b):
    """docstring for function sub"""
    return a - b

##
# @brief Function multiplies 2 numbers.
#
# @param a First factor.
# @param b Second factor.
#
# @return The product of both parameters.
def deus_mult(a, b):
    """docstring for function mult"""
    return a * b

##
# @brief Function divides a by b.
#
# @param a Dividend.
# @param b Divisor.
#
# @return The result of the division of parameters.
def deus_div(a, b):
    """docstring for function div"""
    return a / b

##
# @brief Function calculates the a to the power of b.
#
# @param a Base.
# @param b Exponent.
#
# @return a to the power of b (a^b).
def deus_pow(a, b):
    return a ** b

##
# @brief Function calculates the bth root of a number a.
#
# @param a Base.
# @param b Degree.
#
# @return bth root of a number a.
def deus_root(a, b):
    return a ** (1 / b)

##
# @brief Function recursively calculates factorial.
#
# @param fac Number from which the factorial will be calculated.
#
# @return The product of all positive integers less than or equal to fac (fac!).
# @return -1 if an error occured.
def deus_fact_rec(fac):
	if fac < 0
		return -1
    if fac == 1 or fac == 0:
        return 1
    return fac*deus_fact_rec(fac - 1)

##
# @brief Function iteratively calculates factorial.
#
# @param fac Number from which the factorial will be calculated.
#
# @return The product of all positive integers less than or equal to fac (fac!).
# @return -1 if an error occured.
def deus_fact_ite(fac):
	if fac < 0
		return -1
    if fac == 0:
        return 1
    res = 1
    for x_var in range(1, fac + 1):
        res *= x_var
    return res

##
# @brief Function calculates the logarithm of a with the base b.
#
# @param a Real number.
# @param b Base.
#
# @return The logarithm of a with the base b.
def deus_log(a,b):
    return log(a,b)

##
# @brief Function returns natural logarithm of x.
#
# @param x Real number.
#
# @return The logarithm of x with the base e(=~ 2.71828182846).
def deus_ln(x):
    return log(x)

##
# @brief Function turns x into its absolute value.
#
# @param x Real number.
#
# @return The absolute value of the parameter.
def deus_abs(x):
    if x < 0:
        x = x * (-1)
    return x

##
# @brief Function turns x into its percentage.
#
# @param x Real number.
#
# @return The percentage value of the parameter.
def deus_percent(x):
    return x / 100

# @brief Function turns x into its per mille.
#
# @param x Real number.
#
# @return The per mille value of the parameter.
def deus_permille(x):
    return x / 1000

##
# @brief Function returns 0.
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
# Super secret hidden function,
# which returns the answer to life,
# the universe and everything!
def deus_vult():
    return 42
