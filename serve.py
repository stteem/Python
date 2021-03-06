# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:25:39 2017

@author: Uwemuke
"""

from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    
    #GET
    def do_GET(self):
        
        #send response status code
        self.send_response(200)
        
        #send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        #write message
        self.wfile.write(bytes("hello, world", "utf-8"))
        return
    
# configure server
port = 8080
server_address = ("0.0.0.0", port)
httpd =HTTPServer(server_address, HTTPServer_RequestHandler)

# run server
httpd.serve_forever()