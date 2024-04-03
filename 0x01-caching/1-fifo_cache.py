#!/usr/bin/env python3
"""
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOcache"""
    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
         if key is None or item is None:
            return
