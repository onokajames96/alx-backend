#!/usr/bin/python3
"""module handling LRU"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Class implementing a Least Recently Used (LRU) cache."""

    def __init__(self):
        """ Initialize the LRU cache."""
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or key not in self.cache_data:
            return

        self.cache_data[key] = item
        self.lru_order[key] = item
        self.lru_order.move_to_end(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key, _ = self.lru_order.popitem(last=False)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

    def get(self, key):
        """Retrieve an item from the cach"""
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
