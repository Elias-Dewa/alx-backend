#!/usr/bin/python3
"""LFU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Define a Cache class"""

    def __init__(self):
        """Initialize a class object"""
        super().__init__()
        self.keys = []
        self.values = {}

    def put(self, key, item):
        """A method that assign to the dictionary
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_key = self.keys.index(key)
            del self.cache_data[lfu_key]
            del self.values[lfu_key]
            print("DISCARD: " + lfu_key)
        self.cache_data[key] = item
        if key not in self.keys:
            self.keys.append(key)
            self.values[key] = 0
        else:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.values[key] += 1

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key not in self.cache_data.keys():
            return None
        self.keys.append(self.keys.pop(self.keys.index(key)))
        self.values[key] += 1
        return self.cache_data[key]
