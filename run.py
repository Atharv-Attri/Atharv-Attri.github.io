from http.server import *

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8100)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
