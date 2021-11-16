# ------------------------------------------------- IMPORT DEPENDENCIES ------------------------------------------
try:
    import socket
    import time
except:
    import pip
    pip.main(['install', 'socket', 'time'])
    import socket
    import time

# ------------------------------------------------ CLASS DECLARATIONS -------------------------------------------


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
        """ This function will decrypt a message according to the key provivded """
        output = ''
        for i in string.decode(self.format).split():
            if i != " ":
                try:
                    output = output + self.key[int(i)]
                except:
                    output = output + i
        return output


class ProxyClient:
    def __init__(
        self, 
        port,
        server_ip,
        SECURITY_KEY, 
        crypto_key=' abcdefghijklmnopqrstuvwsyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()><.,:"?{}+=\/-',
        encoding_format='utf-8'
    ):

        """ INIT class. """
        self.ip = server_ip
        self.port = port
        self.client = socket.socket()
        self.key = SECURITY_KEY
        self.format = encoding_format
        self.is_connected = False
        self.encrypter = UniqueProtocol(crypto_key, encoding_format)

    def connect(self):
        """ This function is here to connect with the proxy server.
         usage:

         instance.connect()
         while instance.is_connected():
            ...

         If the while loop doest trigger, it means that the connection was aborted or there was a problem.
        """
        try:
            self.client.connect((self.ip, self.port))
            self.is_connected = True
        except:
            self.is_connected = False

    def send(self, url):
        """ This function is to send a message to the server is a secure way using the encoding format. """
        try:
            url = self.key + " " + url
            self.client.send(self.encrypter.encrypt(url))
            time.sleep(0.01)
        except:
            print('failed to send request to server, the server closed the connection because of suspicious activity.')

    def quit(self):
        """ This function is here to send a proper quit message to the server to properly disconnect. """
        self.client.send(self.encrypter.encrypt('/quit'))
        self.is_connected = False
    
    def get(self):
        """ This function is here to wait until a response is sent. """

        response = self.client.recv(90000000).decode()
        return response
