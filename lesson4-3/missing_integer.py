#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("missing_integer")

def solution(A):
  uniq_array = list(set(A))
  logger.info("This is the passed array %s", A)
  sorted_array = sorted(uniq_array)
  logger.info("This is the sorted array %s", sorted_array)

  positive_array = []
  for number in sorted_array:
    if number > 0:
      positive_array.append(number)
  if not positive_array:
    return 1
  logger.info("This is the positive sorted array %s", positive_array)
  min_value = min(positive_array)
  max_value = max(positive_array)
  logger.info("This is the min value: %d. This is the max value: %d", min_value, max_value)

  if len(positive_array) == 1 and positive_array[0] == 1:
    return 2
  elif len(positive_array) == 1 and positive_array[0] > 1:
    return 1
  elif min_value > 1:
    return 1

  counter_value = min_value
  for number in positive_array:
    if number == counter_value:
      counter_value += 1
    else:
      return counter_value

  return max_value + 1
