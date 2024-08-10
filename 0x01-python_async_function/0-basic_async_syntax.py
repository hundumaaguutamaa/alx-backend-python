#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The amount of time the coroutine waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

