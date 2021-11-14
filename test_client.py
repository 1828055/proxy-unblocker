from client.ProxyBackend.client import *

client = ProxyClient(
    5050,
    socket.gethostbyname(socket.gethostname()),
    SECURITY_KEY='abc123'
)

client.connect()
while client.is_connected:
    url = input('> ')
    if url == '/quit':
        client.quit()
    else:
        client.send(url)
