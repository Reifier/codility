#!/usr/bin/env python

from max_counters import *
import unittest

class TestMaxCounters(unittest.TestCase):
  def testFirstExample(self):
    self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))

unittest.main()
