#!/usr/bin/env python3
"""
runtine execution
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ return runtine execution """
    tp1 = time.time()
    result = [async_comprehension() for loop in range(4)]
    await asyncio.gather(*result)
    return (time.time() - tp1)
