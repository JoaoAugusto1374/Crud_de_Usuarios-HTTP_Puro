from http.server import HTTPServer, BaseHTTPRequestHandler
from server.router import Router

router = Router()

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        router.handle(self, "GET")

    def do_POST(self):
        router.handle(self, "POST")

class Server:
    def __init__(self):
        self.server = HTTPServer(("localhost", 8000), ServerHandler)

    def route(self, path, methods=["GET"]):
        def wrapper(func):
            router.add_route(path, func, methods)
            return func
        return wrapper

    def start(self):
        print("Servidor rodando em http://localhost:8000")
        self.server.serve_forever()
