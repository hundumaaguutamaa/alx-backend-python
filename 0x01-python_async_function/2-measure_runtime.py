#!/usr/bin/env python3
import asyncio
import time
from typing import List
from your_previous_module import wait_n  # Replace 'your_previous_module' with the actual module name

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average time taken for wait_n(n, max_delay) execution.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n
