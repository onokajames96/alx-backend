#!/usr/bin/env python3
"""
Function index_range
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> tuple:
    """Pagination of index range function"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset
        (i.e. the correct list of rows).
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing"""
        data = self.get_page(page, page_size)
        page_size = len(data)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {"page_size": page_size, "page": page,
                "data": data, "next_page": next_page,
                "prev_page": prev_page, "total_pages": total_pages
                }


if __name__ == "__main__":
    server = Server()
