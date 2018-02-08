#!/usr/bin/env python

from missing_integer import *
import unittest

class TestMissingInteger(unittest.TestCase):
  def testSequentialArray(self):
    self.assertEqual(5, solution([1, 2, 3, 4]))

  def testSequentialWithNegatives(self):
    self.assertEqual(2, solution([-3, -2, -1, 0, 1]))

  def testSequentialWithNegativesWithoutZero(self):
    self.assertEqual(2, solution([-3, -2, -1, 1]))

  def testSequentialWithNegativesOnly(self):
    self.assertEqual(1, solution([-3, -2, -1]))

  def testNonSequential(self):
    self.assertEqual(4, solution([1, 2, 3, 5]))

  def testMinimumValueAboveOne(self):
    self.assertEqual(1, solution([2, 3, 4, 5]))

  def testDuplicates(self):
    self.assertEqual(5, solution([1, 3, 6, 4, 1, 2]))

  def testSingleElementArrayOneValue(self):
    self.assertEqual(2, solution([1]))

  def testSingleElementArrayThreeValue(self):
    self.assertEqual(2, solution([3]))

  def testSingleElementArrayThreeValue(self):
    self.assertEqual(1, solution([4, 5, 6, 2]))

  def testExtremelyLargeNumber(self):
    self.assertEqual(1, solution([99999]))

unittest.main()
