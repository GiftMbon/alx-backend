#!/usr/bin/python3
""" lifo caching """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """lifo caching"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign new value to dictionary"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = list(self.cache_data.keys())[-1]
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item

    def get(self, key):
        """returns value"""
        return self.cache_data.get(key)
