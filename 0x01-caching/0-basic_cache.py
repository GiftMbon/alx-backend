#!/usr/bin/python3
""" base caching """
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """basic caching"""

    def put(self, key, item):
        """assign new item to dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return value"""
        return self.cache_data.get(key)
