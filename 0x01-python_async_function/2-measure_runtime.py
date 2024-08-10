#!/usr/bin/env python3
"""
This module measures the runtime of executing a specified number of
asynchronous tasks using the `wait_n` coroutine.
"""

import time
import asyncio
from typing import Union  # Import typing for type annotations
wait_n = __import__('1-concurrent_coroutines').wait_n


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
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
