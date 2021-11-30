from server.ProxyBackend.server import *
import urllib3
from bs4 import BeautifulSoup


def http(request):
    http_proxy = urllib3.PoolManager()
    response = http_proxy.request(method='GET', url=request.split()[1])

    if response.status == 200:
        print('[*] SENDING RESPONSE...')
        soup = BeautifulSoup(response, 'html.parser')
        return soup.prettify()
    else:
        print("[*] Failed to send response to client...")
        error = open('404.html', 'r')
        return error.read()


if __name__ == '__main__':
    server = Proxy(5050, 'USA')
    # start server:
    server.initialize()
    print('STARTING SERVER...')
    server.start(function=http, SECURITY_KEY='abc123')
