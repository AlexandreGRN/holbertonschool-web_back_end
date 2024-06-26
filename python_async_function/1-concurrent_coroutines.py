#!/usr/bin/env python3
"""
return the list of all the delays
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """ return the list of all the delays """
    result = [wait_random(max_delay) for i in range(n)]
    return sorted(await asyncio.gather(*result))
