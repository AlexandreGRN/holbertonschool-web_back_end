#!/usr/bin/env python3
""" 
concurrent coroutine 
"""


import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """ measure_time function """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
