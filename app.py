#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import os
from flask import Flask
from flask_restful import Api, Reource, reqparse

app = Flask(__name__)
api = Api(app)
PORT = 9000

web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()

