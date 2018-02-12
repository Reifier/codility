#!/usr/bin/env python3

import logging
import math

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("count_div")

def solution(A, B, K):
  if A == B == 0:
    logger.info("The edge case where our set is range 0")
    return 1
  if B < K:
    logger.info("The check revealed that number B which is %d is less than number K which is %d", B, K)
    return 0
  logger.info("The integer A is %d. Integer B is %d. Integer K is %d", A, B, K)
  if A == B:
    logger.info("Our range only consists of one number %d, thus testing if it is divisible by %d", B, K)
    result = 1 if B % K == 0 else 0
    return int(result)
  if K == 0 and A == B:
    logger.info("Accounting for a special case where A == B and K == 0")
    return 1
  lowest_number = A if A % K == 0 else A + A % K
  if K > A:
    lowest_number = A + (K - A)
  highest_number = B if B % K == 0 else B - B % K
  logger.info("The lowest divisible number of the set is %d. The highest divisible number of the set is %d", lowest_number, highest_number)
  add_zero = 0
  if A == 0:
    add_zero = 1
  result = (highest_number / K - lowest_number / K) + 1 + add_zero
  logger.info("The result is %d", result)
  return int(result)
