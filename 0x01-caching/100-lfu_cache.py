#!/usr/bin/python3
"""LFU caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache"""

    def __init__(self):
        """initialize with parent's init method"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """assign a new value key pair"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.freq.values())
                least_freq_keys = [
                    k for k, v in self.freq.items() if v == min_freq
                ]
                lfu_key = min(least_freq_keys, key=self.freq.get)
                self.cache_data.pop(lfu_key)
                self.freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = item
            self.freq[key] = 1

    def get(self, key):
        """return value"""
        if key in self.cache_data:
            self.freq[key] += 1
            return self.cache_data.get(key)
