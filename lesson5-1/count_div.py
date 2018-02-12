#!/usr/bin/env python

import logging
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("count_div")

def solution(A, B, K):
  logger.info("The integer A is %d. Integer B is %d. Integer K is %d", A, B, K)
  zero_factor = 0 if A == 0 else 1
  logger.info("This is what will be added to the end result %d", zero_factor)
  result = math.ceil((B - A)/K) + zero_factor
  logger.info("The result is %d", result)
  return result
