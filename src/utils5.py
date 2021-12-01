from http.server import BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers

        message = '¡Hola, mundo!'
        self.wfile.write(bytes(message, 'utf8'))