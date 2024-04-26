#!/usr/bin/env python3
"""module fof handling LIFOCache """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class implementing a LIFO (Last-In, First-Out) cache."""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.last_item_key = None

    def put(self, key, item):
        """ Add an item to the cache."""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = self.last_item_key
            print("DISCARD:", discarded_key)
            del self.cache_data[discarded_key]

        self.last_item_key = key

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
