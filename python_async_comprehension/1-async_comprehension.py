#!/usr/bin/env python3
"""
function that create a list à to 10 with async comprehension
"""
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """ function that create a list à to 10 with async comprehension """
    return [data async for data in async_generator()]
