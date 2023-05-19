#!/usr/bin/python3
"""FIFO caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Define a cache class
    """

    def __init__(self):
        """Initialize a class object"""
        super().__init__()
        self.indexKeys = []

    def put(self, key, item):
        """A method that assign to the dictionary
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            fifo_key = self.indexKeys.pop(0)
            del self.cache_data[fifo_key]
            print("DISCARD: " + fifo_key)

        if item and key:
            self.indexKeys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
