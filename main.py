from server import Server

if __name__ == "__main__":
    server = Server()
    server.setup_insecure_server()
    server.serve()