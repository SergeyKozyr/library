import json
from typing import TypedDict, Iterator
from more_itertools import chunked


class Book(TypedDict):
    title: str
    author: str
    img_src: str
    book_path: str
    comments: list[str]
    genres: str


def get_books(metadata_path: str) -> Iterator[list[Book]]:
    with open(metadata_path, "r") as f:
        books = json.load(f)
    return chunked(books, len(books) // 2)
