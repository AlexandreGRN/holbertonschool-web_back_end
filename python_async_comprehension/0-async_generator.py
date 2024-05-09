#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ asynchronous coroutine """

    for number in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
