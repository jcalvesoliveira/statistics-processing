from server import Server
from prometheus_client import start_http_server

PROMETHEUS_PORT = 5001

if __name__ == "__main__":
    server = Server()
    server.setup_insecure_server()
    start_http_server(PROMETHEUS_PORT)
    server.serve()