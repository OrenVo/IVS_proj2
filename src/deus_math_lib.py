#!/usr/bin/python
# -*- coding: utf-8 -*-
"""docstring for .deus_math_lib"""

##
# @brief Funkce sčítá 2 čísla
#
# @param a První sčítanec.
# @param b Druhý sčítanec.
#
# @return Součet obou parametrů.
def deus_sum(a, b):
    """docstring for function deus_sum"""
    return a + b

##
# @brief Funkce odčítá 2 čísla
#
# @param a Menšenec.
# @param b Menšitel.
#
# @return Rozdíl parametrů.
def deus_sub(a, b):
    """docstring for function sub"""
    return a - b

##
# @brief Funkce dělí 2 čísla
#
# @param a Dělenec.
# @param b Dělitel.
#
# @return Podíl obou parametrů.
def deus_div(a, b):
    return a / b

##
# @brief Funkce násobí 2 čísla
#
# @param a První činitel.
# @param b Druhý činitel.
#
# @return Součin obou parametrů.
def deus_mult(a, b):
    return a * b

##
# @brief Funkce rekurzivně počítá faktoriál.
#
# @param fac Číslo ze kterého se bude počítat faktoriál.
#
# @return Hodnotu faktoriálu z čísla fac (fac!).
def deus_fact_rec(fac):
    if fac == 1 or fac == 0:
        return 1
    return fac*deus_fact_rec(fac - 1)

##
# @brief Funkce iterativně počítá faktoriál.
#
# @param fac Číslo ze kterého se bude počítat faktoriál.
#
# @return Hodnotu faktoriálu z čísla fac (fac!).
def deus_fact_ite(fac):
    if fac == 0:
        return 1
    res = 1
    for x_var in range(1, fac + 1):
        res *= x_var
    return res

##
# @brief Funkce počítá b mocninu z čísla a.
#
# @param a Mocněnec.
# @param b Mocnitel.
#
# @return Mocninu a^b.
def deus_pow(a, b):
    return a ** b

##
# @brief Funkce počítá b odmocninu z čísla a.
#
# @param a Základ odmocnina.
# @param b odmocnitel.
#
# @return B-tá odmocnina.
def deus_root(a, b):
    return a ** (1 / b)
