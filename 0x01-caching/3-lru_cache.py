#!/usr/bin/python3
""" LRU caching """
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign new item to dictionary"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.order.pop(0)
                self.cache_data.pop(removed)
                print("DISCARD: {}".format(removed))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """return value"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return
