from server.ProxyBackend.server import *


def http(request):
    print(request)
    return request


if __name__ == '__main__':
    server = Proxy(5050, 'USA')
    # start server:
    server.initialize()
    print('STARTING SERVER...')
    server.start(function=http, SECURITY_KEY='abc123')

