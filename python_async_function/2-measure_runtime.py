#!/usr/bin/env python3
""" 
concurrent coroutine 
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """ measure_time function """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
