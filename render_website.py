from livereload import Server
from utils import render_pages


if __name__ == "__main__":
    render_pages()
    server = Server()
    server.watch("template.html", render_pages)
    server.serve(root=".", default_filename="./pages/index1.html")
