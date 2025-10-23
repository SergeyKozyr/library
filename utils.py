import json
import os
from typing import TypedDict, Iterator, Sequence, Iterable

from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked

METADATA_PATH = "meta_data.json"
ENV = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"]))


class Book(TypedDict):
    title: str
    author: str
    img_src: str
    book_path: str
    comments: list[str]
    genres: str


def split_in_chunks(iterable: Sequence, chunks: int) -> Iterator[list[Book]]:
    return chunked(iterable, chunks)


def load_books(chunks: int) -> Iterator[list[Book]]:
    with open(METADATA_PATH, "r") as f:
        books = json.load(f)
    return split_in_chunks(books, chunks)


def render_pages():
    os.makedirs("pages", exist_ok=True)
    template = ENV.get_template("template.html")
    books = load_books(20)

    for index, page in enumerate(books, start=1):
        paginated_books = split_in_chunks(page, 2)
        rendered_page = template.render(books=paginated_books)

        with open(f"pages/index{index}.html", "w", encoding="utf8") as file:
            file.write(rendered_page)