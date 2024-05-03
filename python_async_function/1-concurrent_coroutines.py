#!/usr/bin/env python3
""" 
concurrent coroutine 
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ concurrent coroutine """
    result = [wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))
