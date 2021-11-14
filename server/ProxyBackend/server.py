# --------------------------------------------------- GET DEPENDENCIES -----------------------------------------------
from typing import List, Any

try:
    import socket
    import threading
except:
    import pip
    pip.main(['install', 'sockets', 'threading'])
    import socket
    import threading

# --------------------------------------------------- CLASS DECLARATIONS -----------------------------------------------


class Proxy:
    def __init__(self, port, location):
        """ INIT class: """
        self.server_ip = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket()
        self.port = port
        self.address = (self.server_ip, self.port)
        self.total_clients = threading.activeCount() - 1
        self.location = location

    def initialize(self):
        """ This function lets you create your own server, please use the ip provided properly."""

        try:
            self.server.bind(self.address)
            return self.address
        except:
            return None

    def start(self, function, SECURITY_KEY, decoding_format='utf-8'):
        """ This function is responsible to start the whole loop of request and response, it will take an
        argument regarding what function to run when dealt with a request. the input function must have one
        argument, which is the request, and must return a response"""

        def client(conn, addr):
            print('[*] NEW CLIENT CONNECTED')
            while True:
                request = conn.recv(8100).decode(decoding_format)
                if SECURITY_KEY in request:
                    http_handler = function
                    conn.send(http_handler(request).encode(decoding_format))
                elif request == '/quit':
                    print('[*] CLIENT DISCONNECTED')
                    break
                else:
                    print('[*] SUSPICIOUS CLIENT, disconnecting immediately')
                    break
            conn.close()

        self.server.listen()
        while True:
            connection, address = self.server.accept()
            thread = threading.Thread(target=client, args=(connection, address))
            thread.start()
