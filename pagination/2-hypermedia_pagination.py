#!/usr/bin/env python3
"""
simple pagination process
"""

import csv
import math
from typing import List, Tuple, Dict


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
        """ Server class to paginate a database of popular baby names. """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0 and page_size > 0
        self.dataset()
        t = self.index_range(page, page_size)
        if page > len(self.__dataset):
            return []
        return self.__dataset[t[0]:t[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, str]:
        """ Server class to paginate a database of popular baby names. """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0 and page_size > 0
        self.dataset()
        t = self.index_range(page, page_size)
        datas = self.__dataset[t[0]: t[1]]
        next_page_data = self.__dataset[t[0] + page_size : t[1] + page_size]
        previous_page_data = []
        if page != 1:
            previous_page_data = self.__dataset[t[0] - page_size : t[1] - page_size]
        next_page = page + 1 if len(next_page_data) > 0 else None
        previous_page = page - 1 if len(next_page_data) > 0 else None
        return { "page_size": len(datas), "page": page, "data": datas, "next_page": next_page, "prev_page": previous_page, "total_pages": int(len(self.__dataset) / page_size) + (len(self.__dataset) % page_size > 0)}

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """ return the index range of a specific page knowing page sizes """
        return ((page - 1) * page_size, page * page_size)
