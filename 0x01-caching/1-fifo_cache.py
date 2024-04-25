#!/usr/bin/env python3
"""
Class FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache"""

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """Assign to dict"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """Gets data"""
        return self.cache_data.get(key, None)
