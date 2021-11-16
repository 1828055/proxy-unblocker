from urllib.parse import urljoin
from client.ProxyBackend.client import *
import webbrowser
from bs4 import BeautifulSoup as bs


client = ProxyClient(
    5050,
    socket.gethostbyname(socket.gethostname()),
    SECURITY_KEY='abc123'
)

client.connect()
while client.is_connected:
    url = input('>> ')
    if url == '/quit':
        client.quit()
    else:
        client.send(url)
        print('[*] GETTING RESPONSE...')
        response = client.get()

        # export html:
        encoding = 'utf-8'
        file = open('index.html', 'w', encoding=encoding)
        try:
            file.write(response)
        except:
            encoding = 'windows-1525'
            file.write(response)
        file.close()

        soup = bs(response, 'html.parser')

        # get links for css and javascript files and export them:

        script = []

        for scr in soup.find_all("script"):
            if scr.attrs.get("src"):
                script_url = urljoin(url, scr.attrs.get("src"))
                script.append(script_url)

        css_files = []

        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                css_url = urljoin(url, css.attrs.get('href'))
                css_files.append(css_url)

        webbrowser.open_new_tab('index.html')
