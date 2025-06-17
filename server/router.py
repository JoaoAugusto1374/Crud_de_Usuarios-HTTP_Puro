from server.plumbing import extract_path_params

class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, path, func, methods):
        self.routes.append({"path": path, "func": func, "methods": methods})

    def handle(self, request, method):
        path = request.path

        for route in self.routes:
            if route["path"] == path and method in route["methods"]:
                return route["func"](request, request)

            # Suporte simples para rotas com <id> (exemplo: /usuarios/1)
            if "<id>" in route["path"]:
                base_path = route["path"].split("<id>")[0]
                if path.startswith(base_path) and method in route["methods"]:
                    id = path.replace(base_path, "").split("/")[0]
                    return route["func"](request, request, id)

        request.send_response(404)
        request.end_headers()
        request.wfile.write(b"Rota nao encontrada.")
