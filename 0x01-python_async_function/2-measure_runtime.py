#!/usr/bin/env python3
import time
import asyncio
from previous_file import wait_n  # Replace 'previous_file' with the actual filename

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns the average time per call.

    Args:
        n (int): The number of times to run wait_random.
        max_delay (int): The maximum delay for each wait_random call.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate the total execution time
    return total_time / n  # Return the average time per call
