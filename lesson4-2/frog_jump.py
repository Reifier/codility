#!/usr/bin/env python
import logging
import collections

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("frogjump")

def solution(X, A):
  logger.info("The original array %s", A)
  logger.info("The number of steps through the river is: %d", X)

  positions_and_seconds = {}
  for second, position in enumerate(A):
    logger.info("This is the current second: %d, and current position %d", second, position)
    if position not in positions_and_seconds:
      logger.info("The position %d is not in the dictionary %s", position, positions_and_seconds)
      positions_and_seconds[position] = second
    else:
      logger.info("The position %d is already in the dictionary %s", position, positions_and_seconds)
  ordered_positions_and_seconds = collections.OrderedDict(sorted((positions_and_seconds.items())))
  logger.info("This is the ordered dictionary %s", ordered_positions_and_seconds)

  for position in range(1, X + 1):
    if position in ordered_positions_and_seconds:
      logger.info("The position %d is in the dictionary %s", position, ordered_positions_and_seconds)
    else:
      logger.info("The position %d is not in the dictionary %s. The dictionary is incomplete", position, ordered_positions_and_seconds)
      return -1
  largest_time = max(positions_and_seconds.values())
  logger.info("This is the largest time: %d in the dictionary: %s", largest_time, positions_and_seconds)
  logger.info("This is the value to return: %d", largest_time)
  return largest_time
