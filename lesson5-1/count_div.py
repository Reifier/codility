#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("count_div")

def solution(A, B, K):
  logger.info("The integer A is %d. Integer B is %d. Integer K is %d", A, B, K)
  result = (B - A)/K + 1
  logger.info("The result is %d", result)
  return result
