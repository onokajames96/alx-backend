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
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.keys_queue.pop(0)
                del self.cache_data[oldest_key]

            self.cache_data[key] = item
            self.keys_queue.append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)
