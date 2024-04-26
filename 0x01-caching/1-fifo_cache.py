#!/usr/bin/env python3
"""
Class FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class implementing a FIFO (First-In, First-Out) cache.
    """

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
