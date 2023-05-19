#!/usr/bin/python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Define a Cache class"""

    def __init__(self):
        """Initialize a class object"""
        super().__init__()
        self.indexKeys = []

    def put(self, key, item):
        """A method that assign to the dictionary
        """
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.indexKeys.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: " + lru_key)

        if item and key:
            if key in self.indexKeys:
                self.indexKeys.remove(key)
            self.cache_data[key] = item
            self.indexKeys.append(key)

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key not in self.cache_data.keys():
            return None
        self.indexKeys.remove(key)
        self.indexKeys.append(key)
        return self.cache_data[key]
