#!/usr/bin/env python3

from count_div import *
import unittest

class TestCountDiv(unittest.TestCase):
  def testExample(self):
    self.assertEqual(3, solution(6, 11, 2))

  def testWithNine(self):
    self.assertEqual(3, solution(1, 9, 3))

  def testTinyRange(self):
    self.assertEqual(0, solution(0, 1, 2))

  def testExtremeIfempty(self):
    self.assertEqual(1, solution(10, 10, 5))
    self.assertEqual(0, solution(10, 10, 7))
    self.assertEqual(0, solution(10, 10, 20))

  def testRegularExample(self):
    self.assertEqual(20, solution(11, 345, 17))

  def testPolarExtremes(self):
    self.assertEqual(2, solution(0, 2000, 2000))

  def test(self):
    self.assertEqual(3, solution(10, 14, 2))

  def testTrivial(self):
    self.assertEqual(2, solution(11, 14, 2))
    self.assertEqual(1, solution(11, 13, 2))

unittest.main()
