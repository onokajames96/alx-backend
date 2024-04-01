#!/usr/bin/env python3
"""
Function Index_range
"""


def index_range(page: int, page_size: int)-> Tuple[]:
    """Pagination of index range function"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
