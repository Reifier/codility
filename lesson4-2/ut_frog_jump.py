#!/usr/bin/env python

from frog_jump import *
import unittest
import collections

class TestFrogJump(unittest.TestCase):
  def testAllPositionsHaveALeaf(self):
    self.assertEqual(4, solution(5, [4, 3, 1, 2, 5]))

  def testNotAllPositionsHaveALeaf(self):
    self.assertEqual(-1, solution(5, [ 4, 3, 5, 2, 5]))

  def testSingleJump(self):
    self.assertEqual(0, solution(1, [1]))

  def testSingleJumpWithoutGoodLeafPosition(self):
    self.assertEqual(-1, solution(1, [4]))

  def testLargeRepetetiveArray(self):
    self.assertEqual(6, solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

  def testExtremeLeaves(self):
    self.assertEqual(-1, solution(5, [1, 1, 1, 1, 1, 1, 1, 1]))

  def testWideRangeOfTimesAndPositions(self):
    self.assertEqual(13, solution(5, [1, 1, 1, 3, 3, 3, 4, 6, 4, 5, 7, 8, 8, 2]))

unittest.main()
