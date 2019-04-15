#!/usr/bin/python
# -*- coding: utf-8 -*-


###############################################################################
# @file test_deus_math_lib.py
# @brief Tests of the library of math functions for the Holy calculator
#
# @authors Roman Fulla (Xfulla00)
# @authors Vojtěch Ulej (xulejv00)
#
# @version 1.0.2
# @date 15.4.2019
###############################################################################


import math
import pytest
import deus_math_lib


###############################################################################
# @defgroup BASICTESTS Basic Operations Tests
# @brief Tests of the basic operations.
# @{
###############################################################################


##
# @brief Tests of the sum function - see: deus_sum()
def test_deus_sum():
    assert deus_math_lib.deus_sum(-99999, -66666) == -166665
    assert deus_math_lib.deus_sum(-4096, 0) == -4096
    assert deus_math_lib.deus_sum(-2048, 3.8) == -2044.2
    assert deus_math_lib.deus_sum(-13, 29) == 16

    assert deus_math_lib.deus_sum(0, -5) == -5
    assert deus_math_lib.deus_sum(0, -0.25) == -0.25
    assert deus_math_lib.deus_sum(0, 0) == 0
    assert deus_math_lib.deus_sum(0, 0.25) == 0.25
    assert deus_math_lib.deus_sum(0, 5) == 5

    assert deus_math_lib.deus_sum(13, 29) == 42
    assert deus_math_lib.deus_sum(2048, 3.8) == 2051.8
    assert deus_math_lib.deus_sum(4096, 0) == 4096
    assert deus_math_lib.deus_sum(99999, -66666) == 33333


##
# @brief Tests of the subtract function - see: deus_sub()
def test_deus_sub():
    assert deus_math_lib.deus_sub(-2805, -1999) == -806
    assert deus_math_lib.deus_sub(-500, 0) == -500
    assert deus_math_lib.deus_sub(-420, 4.2) == -424.2
    assert deus_math_lib.deus_sub(-5, 4) == -9

    assert deus_math_lib.deus_sub(0, -20) == 20
    assert deus_math_lib.deus_sub(0, -9.11) == 9.11
    assert deus_math_lib.deus_sub(0, 0) == 0
    assert deus_math_lib.deus_sub(0, 9.11) == -9.11
    assert deus_math_lib.deus_sub(0, 20) == -20

    assert deus_math_lib.deus_sub(5, 4) == 1
    assert deus_math_lib.deus_sub(420, 4.2) == 415.8
    assert deus_math_lib.deus_sub(500, 0) == 500
    assert deus_math_lib.deus_sub(2805, -1999) == 4804


##
# @brief Tests of the multiply function - see: deus_mult()
def test_deus_mult():
    assert deus_math_lib.deus_mult(-5000, -100) == 500000
    assert deus_math_lib.deus_mult(-4000, 0) == 0
    assert deus_math_lib.deus_mult(-100, 0.5) == -50
    assert deus_math_lib.deus_mult(-42, 10) == -420

    assert deus_math_lib.deus_mult(0, -158) == 0
    assert deus_math_lib.deus_mult(0, -0.1) == 0
    assert deus_math_lib.deus_mult(0, 0) == 0
    assert deus_math_lib.deus_mult(0, 0.1) == 0
    assert deus_math_lib.deus_mult(0, 158) == 0

    assert deus_math_lib.deus_mult(42, 10) == 420
    assert deus_math_lib.deus_mult(100, 0.5) == 50
    assert deus_math_lib.deus_mult(4000, 0) == 0
    assert deus_math_lib.deus_mult(5000, -100) == -500000


##
# @brief Tests of the divide function - see: deus_div()
def test_deus_div():
    assert deus_math_lib.deus_div(-10000, -8) == 1250
    assert math.isnan(deus_math_lib.deus_div(-50, 0))
    assert deus_math_lib.deus_div(-20, 0.25) == -80
    assert deus_math_lib.deus_div(-10, 2) == -5

    assert deus_math_lib.deus_div(0, -50) == 0
    assert deus_math_lib.deus_div(0, -0.5) == 0
    assert math.isnan(deus_math_lib.deus_div(0, 0))
    assert deus_math_lib.deus_div(0, 0.5) == 0
    assert deus_math_lib.deus_div(0, 50) == 0

    assert deus_math_lib.deus_div(10, 2) == 5
    assert deus_math_lib.deus_div(20, 0.25) == 80
    assert math.isnan(deus_math_lib.deus_div(50, 0))
    assert deus_math_lib.deus_div(10000, -8) == -1250


###############################################################################
# @}
# @defgroup ADVANCEDTESTS Advanced Operations Tests
# @brief Tests of the advanced operations.
# @{
###############################################################################


##
# @brief Tests of the power function - see: deus_pow()
def test_deus_pow():
    assert deus_math_lib.deus_pow(-4, -2) == 0.0625
    assert deus_math_lib.deus_pow(-4, 0) == 1
    # assert deus_math_lib.deus_pow(-4,0.5) == 2i
    assert deus_math_lib.deus_pow(-4, 3) == -64
    assert deus_math_lib.deus_pow(-4, 2) == 16

    assert deus_math_lib.deus_pow(0, -10) == 0
    assert deus_math_lib.deus_pow(0, -2.25) == 0
    assert deus_math_lib.deus_pow(0, 0) == 1
    assert deus_math_lib.deus_pow(0, 2.25) == 0
    assert deus_math_lib.deus_pow(0, 10) == 0

    assert deus_math_lib.deus_pow(4, 2) == 16
    assert deus_math_lib.deus_pow(4, 3) == 64
    assert deus_math_lib.deus_pow(4, 0.5) == 2
    assert deus_math_lib.deus_pow(4, 0) == 1
    assert deus_math_lib.deus_pow(4, -2) == 0.0625


##
# @brief Tests of the root function - see: deus_root()
def test_deus_root():
    # assert deus_math_lib.deus_root(-15625,-3) == 0.02 - 0.0346410162i
    assert math.isnan(deus_math_lib.deus_root(-15625, 0))
    assert deus_math_lib.deus_root(-15625, 0.5) == 244140625
    assert deus_math_lib.deus_root(-15625, 3) == -25
    # assert deus_math_lib.deus_root(-15625,2) == 125i

    assert math.isnan(deus_math_lib.deus_root(0, -8))
    assert math.isnan(deus_math_lib.deus_root(0, -0.5))
    assert math.isnan(deus_math_lib.deus_root(0, 0))
    assert deus_math_lib.deus_root(0, 0.5) == 0
    assert deus_math_lib.deus_root(0, 8) == 0

    assert deus_math_lib.deus_root(15625, 2) == 125
    assert deus_math_lib.deus_root(15625, 3) == 25
    assert deus_math_lib.deus_root(15625, 0.5) == 244140625
    assert math.isnan(deus_math_lib.deus_root(15625, 0))
    assert deus_math_lib.deus_root(15625, -3) == 0.04


##
# @brief Tests of the recursive factorial function - see: deus_fact_rec()
def test_deus_fact_rec():
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_rec(-10.5)
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_rec(-5)

    assert deus_math_lib.deus_fact_rec(0) == 1

    assert deus_math_lib.deus_fact_rec(5) == 120
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_rec(10.5)


##
# @brief Tests of the iterative factorial function - see: deus_fact_ite()
def test_deus_fact_ite():
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_ite(-10.5)
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_ite(-5)

    assert deus_math_lib.deus_fact_ite(0) == 1

    assert deus_math_lib.deus_fact_ite(5) == 120
    with pytest.raises(ValueError):
        deus_math_lib.deus_fact_ite(10.5)


##
# @brief Tests of the logarithm function - see: deus_log()
def test_deus_log():
    assert math.isnan(deus_math_lib.deus_log(-5, 10))
    assert math.isnan(deus_math_lib.deus_log(-3.5, 5))

    assert math.isnan(deus_math_lib.deus_log(0, 0))
    assert math.isnan(deus_math_lib.deus_log(0, 1))
    assert math.isnan(deus_math_lib.deus_log(0, 10))

    assert deus_math_lib.deus_log(1, 100) == 0
    assert math.isnan(deus_math_lib.deus_log(1, 1))

    assert deus_math_lib.deus_log(0.25, 2) == -2
    assert deus_math_lib.deus_log(2, 0.25) == -0.5

    assert deus_math_lib.deus_log(10, 10) == 1
    assert deus_math_lib.deus_log(10, 100) == 0.5
    assert deus_math_lib.deus_log(100, 10) == 2

    assert math.isnan(deus_math_lib.deus_log(500, 0))
    assert math.isnan(deus_math_lib.deus_log(1000, -5))
    assert math.isnan(deus_math_lib.deus_log(1000, -3.5))

    assert math.isnan(deus_math_lib.deus_log(0, math.e))
    assert deus_math_lib.deus_log(0.5, math.e) == math.log(0.5)
    assert deus_math_lib.deus_log(1, math.e) == 0
    assert deus_math_lib.deus_log(5, math.e) == math.log(5)


###############################################################################
# @}
# @defgroup NADJUSTMENTSTESTS Number Adjusting Operations Tests
# @brief Tests of the number adjustments.
# @{
###############################################################################


##
# @brief Tests of the absolute function - see: deus_abs()
def test_deus_abs():
    assert deus_math_lib.deus_abs(-96969) == 96969
    assert deus_math_lib.deus_abs(-10) == 10
    assert deus_math_lib.deus_abs(-5.55) == 5.55

    assert deus_math_lib.deus_abs(0) == 0

    assert deus_math_lib.deus_abs(5.55) == 5.55
    assert deus_math_lib.deus_abs(10) == 10
    assert deus_math_lib.deus_abs(96969) == 96969


##
# @brief Tests of the percentage function - see: deus_percent()
def test_deus_percent():
    assert deus_math_lib.deus_percent(-999999) == -9999.99
    assert deus_math_lib.deus_percent(-128) == -1.28
    assert deus_math_lib.deus_percent(-10.5) == -0.105

    assert deus_math_lib.deus_percent(0) == 0

    assert deus_math_lib.deus_percent(10.5) == 0.105
    assert deus_math_lib.deus_percent(128) == 1.28
    assert deus_math_lib.deus_percent(999999) == 9999.99


##
# @brief Tests of the promille function - see: deus_promille()
def test_deus_promille():
    assert deus_math_lib.deus_promille(-20042001) == -20042.001
    assert deus_math_lib.deus_promille(-1024) == -1.024
    assert deus_math_lib.deus_promille(-100.5) == -0.1005

    assert deus_math_lib.deus_promille(0) == 0

    assert deus_math_lib.deus_promille(100.5) == 0.1005
    assert deus_math_lib.deus_promille(1024) == 1.024
    assert deus_math_lib.deus_promille(20042001) == 20042.001


###############################################################################
# @}
# @defgroup CONSTATNTSTESTS Constants Tests
# @brief Tests of the constants.
# @{
###############################################################################


##
# @brief Test of the clear function - see: deus_clear()
def test_deus_clear():
    assert deus_math_lib.deus_clear() == 0


##
# @brief Test of the e function - see: deus_e()
def test_deus_e():
    assert deus_math_lib.deus_e() == math.e


##
# @brief Test of the Pi function - see: deus_pi()
def test_deus_pi():
    assert deus_math_lib.deus_pi() == math.pi


##
# @brief Test of the random function - see: deus_rnd()
def test_deus_rnd():
    assert deus_math_lib.deus_rnd() != deus_math_lib.deus_rnd()


def test_deus_vult():
    assert deus_math_lib.deus_vult() == 42


###############################################################################
# @}
# End of the test_deus_math_lib.py
###############################################################################
