from livereload import Server
from utils import render_pages

render_pages()
server = Server()
server.watch("template.html", render_pages)
server.serve(root=".")
