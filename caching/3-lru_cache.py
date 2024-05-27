#!/usr/bin/env python3
""" implementation of a LRU caching system """
BasicCache = __import__('0-basic_cache').BasicCache


class LRUCache(BasicCache):
    """ LRU cache class """
    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                first = keys[0]
                print("DISCARD: {}".format(first))
                del self.cache_data[first]

    def get(self, key):
        """ get an item by key """
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return item
