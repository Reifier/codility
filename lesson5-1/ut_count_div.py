#!/usr/bin/env python

from count_div import *
import unittest

class TestCountDiv(unittest.TestCase):
  def testExample(self):
    self.assertEqual(2, solution(6, 11, 3))

  def testWithNine(self):
    self.assertEqual(3, solution(1, 9, 3))






unittest.main()
