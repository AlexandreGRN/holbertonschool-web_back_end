#!/usr/bin/env python3
""" implementation of a LIFO caching system """
BasicCache = __import__('0-basic_cache').BasicCache


class LIFOCache(BasicCache):
    """ LIFO cache class """
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
                last = keys[self.MAX_ITEMS - 1]
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """ get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
