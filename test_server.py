from server.ProxyBackend.server import *
import urllib3


def http(request):
    http_proxy = urllib3.PoolManager()
    response = http_proxy.request(method='GET', url=request.split()[1])

    if response.status == 200:
        print('[*] SENDING RESPONSE...')
        try:
            return response.data.decode('utf-8')
        except:
            return response.data.decode('windows-1525')
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
