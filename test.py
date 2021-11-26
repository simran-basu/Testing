from unittest import TestCase
from unittest.mock import patch
import Calculator_2
#from Calculator_2 import Sci_Calculator
import numpy as np
import mock
import builtins
import math


class CalcTest(TestCase):

    pi = 22/7

    def testFact(self):
        self.assertEqual(Calculator_2.Factorial(5),120)

    def testFact2(self):
        self.assertEqual(Calculator_2.Factorial(0),1)

    def testFloor(self):
        self.assertEqual(Calculator_2.Floor(2.5),2)

    def testFloor1(self):
        self.assertEqual(Calculator_2.Floor(2),2)

    def testFloor2(self):
        self.assertEqual(Calculator_2.Floor(-2.5),-3)

    def testFloor3(self):
        self.assertEqual(Calculator_2.Floor(0),0)

    def testCeil(self):
        self.assertEqual(Calculator_2.Ceil(2.3),3)

    def testCeil1(self):
        self.assertEqual(Calculator_2.Ceil(2),2)

    def testCeil2(self):
        self.assertEqual(Calculator_2.Ceil(-2.3),-2)

    def testCeil3(self):
        self.assertEqual(Calculator_2.Ceil(0),0)

    def testGCD(self):
        self.assertEqual(Calculator_2.GCD(5,8),1)

    def testPerm(self):
        self.assertEqual(Calculator_2.perm(5,2),20)

    def testComb(self):
        self.assertEqual(Calculator_2.comb(5,2),10)

    def testPerm1(self):
        self.assertEqual(Calculator_2.perm(5,5),120)

    def testComb2(self):
        self.assertEqual(Calculator_2.comb(5,5),1)

    def testSqrt(self):
        self.assertEqual(Calculator_2.Sqrt(4),2)

    def testSqrt1(self):
        self.assertEqual(Calculator_2.Sqrt(0),0) 

    def testSin(self):
        self.assertAlmostEqual(round(Calculator_2.Sin(self.pi/2)),1)

    def testCos(self):
        self.assertAlmostEqual(round(Calculator_2.Cos(0)),1) 

    def testTan(self):
        self.assertAlmostEqual(round(Calculator_2.Tan(self.pi/4)),1)

    def testLCM(self):
        original_input=builtins.input
        builtins.input=lambda _: '120 60 40'
        self.assertEqual(Calculator_2.LCM(),120)
        builtins.input = original_input

    def test_fmod(self):
        self.assertEqual(Calculator_2.fmod(5,5),0.0)

    def test_Roots(self):
        with mock.patch.object(builtins, 'input', lambda _: '3 1 -2'):
            res = [-1.0,1.5]
            np.testing.assert_array_almost_equal(Calculator_2.Roots(),res)
    
    def test_log(self):
        self.assertEqual(Calculator_2.Log(math.e),1)