#!/usr/bin/env python3
"""
now returns asyncio.Task.
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ async object """
    return asyncio.Task(wait_random(max_delay))
