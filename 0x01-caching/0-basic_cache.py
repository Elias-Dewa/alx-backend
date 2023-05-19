#!/usr/bin/python3
"""a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BaseCache(BaseCaching):
    """Define a cache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """A method that assign to the dictionary
        """
        if item and key:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key
        """
        if key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
