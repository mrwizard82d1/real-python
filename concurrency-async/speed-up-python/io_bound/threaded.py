import concurrent.futures
import threading
import time

import requests


thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()

    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as _response:
        indicator = 'J' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)


def download_sites(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_site, urls)


if __name__ == '__main__':
    sites = [
        'https://www.jython.org',
        'http://olympus.realpython.org/dice',
    ] * 80

    print('Downloading sites...')
    start = time.time()
    download_sites(sites)
    duration = time.time() - start
    print(f'\nDownloaded {len(sites)} sites in {duration} seconds')
