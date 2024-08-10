#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of executing
a specified number of async tasks using the `wait_n` coroutine.
"""

import time
import asyncio
from wait_n import wait_n
from typing import Union


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average time taken for wait_n(n, max_delay) execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
