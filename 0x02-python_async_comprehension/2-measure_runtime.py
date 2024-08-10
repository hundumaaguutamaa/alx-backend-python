#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a coroutine
called measure_runtime that will execute async_comprehension four times
in parallel using asyncio.gather. measure_runtime should measure the total
runtime and return it.
"""

import asyncio
import time
from typing import List

# Import async_comprehension from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time

