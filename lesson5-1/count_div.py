#!/usr/bin/env python3

import logging
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("count_div")

def solution(A, B, K):
  if B < K:
    logger.info("The check revealed that number B which is %d is less than number K which is %d", B, K)
    return 0
  logger.info("The integer A is %d. Integer B is %d. Integer K is %d", A, B, K)
  if A == B:
    logger.info("Our range only consists of one number %d, thus testing if it is divisible by %d", B, K)
    result = 1 if B % K == 0 else 0
    return result
  lowest_number = A if A % K == 0 else A + K - A
  highest_number = B if B % K == 0 else B - B % K
  logger.info("The lowest divisible number of the set is %d. The highest divisible number of the set is %d", lowest_number, highest_number)
  result = (highest_number / K - lowest_number / K) + 1
  logger.info("The result is %d", result)
  return result
