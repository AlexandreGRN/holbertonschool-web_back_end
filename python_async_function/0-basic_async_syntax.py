#!/usr/bin/env python3
""" 
asynchronous coroutine 
"""
import asyncio
import random

async def wait_random(max_delay=10):
    """ asynchronous coroutine """
    seconds = random.uniform(0, max_delay)
    await asyncio.sleep(seconds)
    return seconds
