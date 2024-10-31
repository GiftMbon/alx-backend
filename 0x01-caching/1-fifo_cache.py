#!/usr/bin/python3
"""fifo caching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """fifo caching"""

    def __init__(self):
        """assign """
        super().__init__()

    def put(self, key, item):
        """assign new item to dictionary"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = next(iter(self.cache_data))
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """return value """
        return self.cache_data.get(key)
