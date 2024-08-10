#!/usr/bin/env python3
"""
This module provides a function to create an asyncio.Task
from the wait_random coroutine.
"""

import asyncio
from typing import Any
from your_previous_module import wait_random  # Replace with the actual module name

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that wraps the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))

