#!/usr/bin/env python3
"""
helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return the index range of a specific page knowing page sizes """
    return ((page - 1) * page_size, page * page_size)
