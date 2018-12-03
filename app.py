#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import os

PORT = 9000

web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

