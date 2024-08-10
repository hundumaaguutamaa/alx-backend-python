#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task
from the wait_random coroutine.

The task_wait_random function takes an integer max_delay as an argument
and returns an asyncio.Task that wraps the wait_random coroutine.
"""

import asyncio
from typing import Any  # Importing Any for potential future use in type hints
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
