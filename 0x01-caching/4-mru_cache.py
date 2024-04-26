#!/usr/bin/python3
"""module  Caching MRU"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class implementing a Most Recently Used (MRU) cache."""

    def __init__(self):
        """Initialize the MRU cache"""
        super().__init__()
        self.head, self.tail = 'head', 'tail'
        self.next, self.prev = {}, {}
        self.handle(self.head, self.tail)

    def handle(self, head, tail):
        """Initialize the linked list"""
        self.next[head], self.prev[tail] = tail, head

    def _remove(self, key):
        """Remove an element from the cache."""
        self.handle(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def _add(self, key, item):
        """Add an element to the cache"""
        if len(self.cache_data) > self.MAX_ITEMS - 1:
            self._remove(self.prev[self.tail])
        self.cache_data[key] = item
        self.handle(self.prev[self.tail], key)
        self.handle(key, self.tail)

    def put(self, key, item):
        """Add or update an item in the MRU cache."""
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def get(self, key):
        """Retrieve an item from the MRU cache."""
        if key in self.cache_data:
            self.handle(self.prev[key], self.next[key])
            self.handle(self.prev[self.tail], key)
            return self.cache_data[key]
        return None
