from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/workflow':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            with open('.github/workflows/main.yml', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(format % args)

if __name__ == '__main__':
    port = 5000
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f'Server running on http://0.0.0.0:{port}')
    server.serve_forever()
