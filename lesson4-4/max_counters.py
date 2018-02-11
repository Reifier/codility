#!/usr/bin/env python

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("max_counters")

def solution(N, A):
  logger.info("This is the number that was passed %d", N)
  logger.info("This is the array that was passed %s", A)

  counters = [0] * N
  max_counter = 0

  for operation in A:
    logger.info("This is the value of operation: %d", operation)
    if 1 <= operation <= N:
      logger.info("Identified operation as addition")
      counters[operation - 1] += 1
      logger.info("The value of the counter is changed from %d to %d", counters[operation - 1] - 1, counters[operation - 1])
      logger.info("Printing all the counters: %s", counters)
      if counters[operation - 1] > max_counter:
        logger.info("Setting a new max counter to be %d for counters %s", counters[operation - 1], counters)
        max_counter = counters[operation - 1]
    elif operation == N + 1:
      logger.info("The operation is identified to be total maximization")
      counters = [max_counter] * N
      logger.info("End result after main loop %s", counters)

  logger.info("Final end result %s", counters)
  return counters


