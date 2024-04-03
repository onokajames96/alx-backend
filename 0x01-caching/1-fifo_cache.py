#!/usr/bin/env python3
"""
Class module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOcache"""
    def __init__(self):
        """Initialization"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Assign to dict"""
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Gets data"""
        return self.cache_data.get(key, None)
