#!/usr/bin/env python3
"""
simple pagination process
"""

import csv
import math
from typing import List


get_pagination_index = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert 0 < page
        assert 0 < page_size
        (start_index, end_index) = get_pagination_index(page, page_size)
        retuf = open("Popular_Baby_Names.csv ", "r")
        result = []
        i = 0
        for line in retuf:
            if start_index < i <= end_index:
                result.append(line.split(", "))
            i += 1
        return result
