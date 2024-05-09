#!/usr/bin/env python3
"""
The code is nearly identical to wait_n except task_wait_random is being called
"""
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all the delays """
    result = [task_wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))
