#!/usr/bin/env python3
"""
This module contains a coroutine called async_generator
that yields random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously generates and yields 10 random numbers.

    This coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    
    Returns:
        Generator[float, None, None]: A generator that yields random numbers.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

