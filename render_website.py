from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from utils import get_books

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"]))


def on_reload():
    template = env.get_template("template.html")
    rendered_page = template.render(books=get_books("meta_data.json"))

    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)


server = Server()
server.watch("template.html", on_reload)
server.serve(root=".")
