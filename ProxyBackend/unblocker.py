import socket

HEADER = 64
PORT = 9091
SERVER = '45.79.223.43'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

proxy_client = socket.socket()


def get(url):
    print('[*] CONNECTING TO SERVER...')
    proxy_client.connect(ADDR)
    print('[*] REQUESTING WEBSITE...')
    proxy_client.send(url.encode(FORMAT))
    print('[*] GETTING RESPONSE...')
    response = proxy_client.recv(3000)
    print('[*] PROCCESSING RESPONSE...')
    print(response.decode())
    proxy_client.close()


while True:
    request = input("> ")
    # if 'www.' in request:
    #     headers = f"""GET http://{request} HTTPS/1.1
    #                     Host: {request}\r\n\r\n"""
    # else:
    #     headers = f"""GET http://www.{request} HTTPS/1.1
    #                     Host: www.{request}\r\n\r\n"""
    headers = request
    get(headers)
