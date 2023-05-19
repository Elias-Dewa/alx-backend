# 0x01. Caching

## Resources

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## More Info

Parent class BaseCaching
All your classes must inherit from BaseCaching defined below:

    $ cat base_caching.py
    # !/usr/bin/python3
    """ BaseCaching module
    """

    class BaseCaching():
        """ BaseCaching defines:
          - constants of your caching system
          - where your data are stored (in a dictionary)
        """
        MAX_ITEMS = 4

        def __init__(self):
            """ Initiliaze
            """
            self.cache_data = {}

        def print_cache(self):
            """ Print the cache
            """
            print("Current cache:")
            for key in sorted(self.cache_data.keys()):
                print("{}: {}".format(key, self.cache_data.get(key)))

        def put(self, key, item):
            """ Add an item in the cache
            """
            raise NotImplementedError("put must be implemented in your cache class")

        def get(self, key):
            """ Get an item by key
            """
            raise NotImplementedError("get must be implemented in your cache class")

# Solutions for mandatory and advanced tasks
