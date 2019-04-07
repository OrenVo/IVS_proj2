import math
import deus_math_lib

# Need special attention '#':
#  Desatinne mocniny
#
#  Odmocniny z negativnych cisel
#  Odmocniny z 0
#  0tá odmocnina
#
#  Faktoriál - vždy kladné (a celé?)
#
#  Logaritmus - vždy kladný a nenulový

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

def test_deus_div():
    assert deus_math_lib.deus_div(-10000, -8) == 1250
    assert math.isnan(deus_math_lib.deus_div(-50, 0))                       #
    assert deus_math_lib.deus_div(-20, 0.25) == -80
    assert deus_math_lib.deus_div(-10, 2) == -5

    assert deus_math_lib.deus_div(0, -50) == 0
    assert deus_math_lib.deus_div(0, -0.5) == 0
    assert math.isnan(deus_math_lib.deus_div(0, 0))                         #
    assert deus_math_lib.deus_div(0, 0.5) == 0
    assert deus_math_lib.deus_div(0, 50) == 0

    assert deus_math_lib.deus_div(10, 2) == 5
    assert deus_math_lib.deus_div(20, 0.25) == 80
    assert math.isnan(deus_math_lib.deus_div(50, 0))                        #
    assert deus_math_lib.deus_div(10000, -8) == -1250

def test_deus_pow():
    assert deus_math_lib.deus_pow(-4, -2) == 0.0625
    assert deus_math_lib.deus_pow(-4, 0) == 1
    #assert deus_math_lib.deus_pow(-4,0.5) == 2i                            #
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

def test_deus_root():
    #assert deus_math_lib.deus_root(-15625,-3) == 0.02 - 0.0346410162i      #
    assert math.isnan(deus_math_lib.deus_root(-15625, 0))                   #
    assert deus_math_lib.deus_root(-15625, 0.5) == 244140625                #
    assert deus_math_lib.deus_root(-15625, 3) == -25                        #
    #assert deus_math_lib.deus_root(-15625,2) == 125i                       #

    assert math.isnan(deus_math_lib.deus_root(0, -8))                       #
    assert math.isnan(deus_math_lib.deus_root(0, -0.5))                     #
    assert math.isnan(deus_math_lib.deus_root(0, 0))                        #
    assert deus_math_lib.deus_root(0, 0.5) == 0
    assert deus_math_lib.deus_root(0, 8) == 0

    assert deus_math_lib.deus_root(15625, 2) == 125
    assert deus_math_lib.deus_root(15625, 3) == 25
    assert deus_math_lib.deus_root(15625, 0.5) == 244140625
    assert math.isnan(deus_math_lib.deus_root(15625, 0))                    #
    assert deus_math_lib.deus_root(15625, -3) == 0.04

def test_deus_fact_rec():
    assert deus_math_lib.deus_fact_rec(0) == 1
    assert deus_math_lib.deus_fact_rec(5) == 120
    assert deus_math_lib.deus_fact_rec(10.5) == 11899423.084                #

def test_deus_fact_ite():
    assert deus_math_lib.deus_fact_ite(0) == 1
    assert deus_math_lib.deus_fact_ite(5) == 120
    assert deus_math_lib.deus_fact_ite(10.5) == 11899423.084                #

def test_deus_log():
    assert math.isnan(deus_math_lib.deus_log(0, 10))                        #
    assert deus_math_lib.deus_log(0.25, 2) == -2
    assert deus_math_lib.deus_log(1, 100) == 0
    assert deus_math_lib.deus_log(2, 0.25) == -0.5
    assert deus_math_lib.deus_log(10, 10) == 1
    assert deus_math_lib.deus_log(10, 100) == 0.5
    assert deus_math_lib.deus_log(100, 10) == 2

def test_deus_ln():
    assert math.isnan(deus_math_lib.deus_ln(0))                             #
    assert deus_math_lib.deus_ln(0.5) == math.log(0.5)
    assert deus_math_lib.deus_ln(1) == 0
    assert deus_math_lib.deus_ln(5) == math.log(5)

def test_deus_abs():
    assert deus_math_lib.deus_abs(-96969) == 96969
    assert deus_math_lib.deus_abs(-10) == 10
    assert deus_math_lib.deus_abs(-5.55) == 5.55

    assert deus_math_lib.deus_abs(0) == 0

    assert deus_math_lib.deus_abs(5.55) == 5.55
    assert deus_math_lib.deus_abs(10) == 10
    assert deus_math_lib.deus_abs(96969) == 96969

def test_deus_percent():
    assert deus_math_lib.deus_percent(-999999) == -9999.99
    assert deus_math_lib.deus_percent(-128) == -1.28
    assert deus_math_lib.deus_percent(-10.5) == -0.105

    assert deus_math_lib.deus_percent(0) == 0

    assert deus_math_lib.deus_percent(10.5) == 0.105
    assert deus_math_lib.deus_percent(128) == 1.28
    assert deus_math_lib.deus_percent(999999) == 9999.99

def test_deus_permille():
    assert deus_math_lib.deus_permille(-20042001) == -20042.001
    assert deus_math_lib.deus_permille(-1024) == -1.024
    assert deus_math_lib.deus_permille(-100.5) == -0.1005

    assert deus_math_lib.deus_permille(0) == 0

    assert deus_math_lib.deus_permille(100.5) == 0.1005
    assert deus_math_lib.deus_permille(1024) == 1.024
    assert deus_math_lib.deus_permille(20042001) == 20042.001

def test_deus_e():
    assert deus_math_lib.deus_e() == math.e

def test_deus_pi():
    assert deus_math_lib.deus_pi() == math.pi

def test_deus_vult():
    assert deus_math_lib.deus_vult() == 42
