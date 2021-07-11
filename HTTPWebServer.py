from http import server
serverAddress = ("localhost", 8080)
htmlFile = open("./index.html", encoding="utf8")


class ServerHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(htmlFile.read(), "utf-8"))
        htmlFile.seek(0)
        self.wfile.flush()
        #self.wfile.close()


WebServer = server.HTTPServer(serverAddress, ServerHandler)


def foo():
    print("exiting")
    WebServer.server_close()
    print("exited")

WebServer.serve_forever()
