import asyncio

""" 
concurrent coroutine 
"""

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    """ concurrent coroutine """
    result = [wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))
