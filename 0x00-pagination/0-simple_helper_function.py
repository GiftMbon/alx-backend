#!/usr/bin/env python3
""" module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function """
    startPage = (page - 1) * page_size
    endPage = page * page_size
    return (startPage, endPage)
