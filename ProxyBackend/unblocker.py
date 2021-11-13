# --------------------------------------------------- GET DEPENDENCIES -----------------------------------------------
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
    clients = threading.activeCount() - 1

    def __init__(self, port):
        """ INIT class: """
        self.server_ip = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket()
        self.port = port
        self.address = (self.server_ip, self.port)

    def initialize(self):
        """ This function lets you create your own server inside a mini machine, please use the ip provided properly."""

        try:
            self.server.bind(self.address)
            return self.address
        except:
            return None

    def start(self, function, decoding_format, SECURITY_KEY):
        """ This function is responsible to start the whole loop of request and response, this one will take a
        argument regarding what function to run when dealt with a request. the input functions must have one
        argument, which is the request, and must return a response"""

        def client(conn):
            while True:
                request = conn.recv(8100).decode(decoding_format)
                if SECURITY_KEY in request:
                    conn.send(function(request))

        self.server.listen()
        while True:
            connection, address = self.server.accept()
            thread = threading.Thread(target=client, args=connection)
            thread.start()

    def close(self):
        """ This function is here to shut down the server when needed. """
        self.server.close()
