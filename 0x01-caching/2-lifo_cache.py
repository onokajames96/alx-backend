#!/usr/bin/env python3
"""LIFOCache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.last_item_key = None

    def put(self, key, item):
        """ add an item to cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.last_key
            print("DISCARD:", discarded_key)
            del self.cache_data[discarded_key]

        self.last_key = key

    def get(self, key):
        """ Get an item by ket"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
