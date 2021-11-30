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


class UniqueProtocol:
    def __init__(self, key, binary_format):
        """ INIT class (note that key is a string) """
        self.key = key 
        self.format = binary_format

    def encrypt(self, string):
        """ This function will encrypt a message according the key provided """
        output = ''
        for i in list(string):
            try:
                output = output + " " + str(self.key.find(i))
            except:
                output = output + i
        return output.encode(self.format)

    def decrypt(self, string):
        """ This function will decrypt a message according to the key provided """
        output = ''
        for i in string.decode(self.format).split():
            if i != " ":
                try:
                    output = output + self.key[int(i)]
                except:
                    output = output + i
        return output


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
        self.format = decode_format

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
        argument, which is the request, and must return a response. """

        def client(conn, addr):
            print('[*] NEW CLIENT CONNECTED')
            while True:
                request = self.decrypter.decrypt(conn.recv(8100))
                if SECURITY_KEY in request:
                    response = function(request)
                    conn.send(f'{response}'.encode(self.format))
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
