from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        client = self.path.replace("/", "")

        print(f"Client {client} mulai diproses")

        time.sleep(5)

        print(f"Client {client} selesai")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Hello {client}".encode())

server = ThreadingHTTPServer(("localhost", 8000), Handler)
print("Server berjalan di http://localhost:8000")
server.serve_forever()



