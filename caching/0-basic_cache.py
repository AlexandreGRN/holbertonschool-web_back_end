#!/usr/bin/python3
""" basic implementation of a caching system """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basic cache class """
    def put(self, key, item):
        """ add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
