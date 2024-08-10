#!/usr/bin/env python3
"""
This module provides a function to create and run multiple asyncio.Tasks
using the task_wait_random function.

The task_wait_n function spawns task_wait_random n times and returns a list
of delays in the order they are completed.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns the list of delays.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random call.

    Returns:
        List[float]: A list of delays in the order they were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create tasks using task_wait_random
    delays = [await task for task in asyncio.as_completed(tasks)]  # Collect completed tasks' results
    return delays
