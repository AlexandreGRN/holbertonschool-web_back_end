#!/usr/bin/env python3
"""
helper function for pagination
"""
import random


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """ return the index range of a specific page knowing page sizes"""
    return ((page - 1) * page_size, page * page_size)
