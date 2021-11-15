# --------------------------------------------------- GET DEPENDENCIES -----------------------------------------------
from proxy_cryptography.protocols import UniqueProtocol

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
    def __init__(
        self,
        port,
        location, 
        decode_format='utf-8',
        crypto_key=' abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()><.,:"?{}+=\/-',
    ):
        """ INIT class: """
        self.server_ip = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket()
        self.port = port
        self.address = (self.server_ip, self.port)
        self.total_clients = threading.activeCount() - 1
        self.location = location
        self.decrypter = UniqueProtocol(crypto_key, decode_format)

    def initialize(self):
        """ This function lets you create your own server, please use the ip provided properly."""

        try:
            self.server.bind(self.address)
            return self.address
        except:
            return None

    def start(self, function, SECURITY_KEY):
        """ This function is responsible to start the whole loop of request and response, it will take an
        argument regarding what function to run when dealt with a request. the input function must have one
        argument, which is the request, and must return a response"""

        def client(conn, addr):
            print('[*] NEW CLIENT CONNECTED')
            while True:
                request = self.decrypter.decrypt(conn.recv(8100))
                if SECURITY_KEY in request:
                    http_handler = function
                    conn.send(self.decrypter.encrypt(http_handler(request)))
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
