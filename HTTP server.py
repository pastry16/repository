# in this project we will try to make a simple http server in python. 
# to do this, there are two ways, one is a one-liner method, and the other is programmatically
# i will use the longer method.

import http.server
import socketserver

# socketserver and http.server are built-in modules

PORT = 8000

# by default, servers start on port 8000, taking files from the directory

Handler = http.server.simplehttphandler

# simplehttphandler is the default handler that serves files and directories

with socketserver.TCPserver (("", PORT), Handler) as httpd

# socketserver is used to build a http server in python other than the one-liner method
# the above cmd creates a TCP server. the argument helps in accessing all network interfaces available in that port
# this makes the server accessible to all devices under the local network

print (f"Serving at port {PORT}") 

# this command starts the server at the directed port we put earlier.

httpd.serve_forever()

# this command tells the server to be active until we manually stop it.
# and that's all, bye
