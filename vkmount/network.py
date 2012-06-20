# -*- coding: utf-8 -*-

import httplib
from urlparse import urlparse
import logging

def get_size(url):
    '''
    >>> get_size("http://img.yandex.net/i/www/logo.png")
    3729
    '''
    netloc, path = parse_url(url)
    conn = httplib.HTTPConnection(netloc)
    conn.request("HEAD", path)
    res = conn.getresponse()

    if int(res.status) == 200:
        logging.debug("Successful got file size. Url: {0}, size: {1}".format(url, res.getheader('content-length')))
        return int(res.getheader('content-length'))

    # TODO обработка ошибок

def get_file(url):
    '''
    >>> len(get_file("http://img.yandex.net/i/www/logo.png"))
    3729
    '''
    netloc, path = parse_url(url)
    conn = httplib.HTTPConnection(netloc)
    conn.request("GET", path)
    response = conn.getresponse()
    body_size = response.getheader("content-length")
    file_size = 0

    body = ""
    chunk_size = 4096
    while True:
        buffer = response.read(chunk_size)
        if not buffer:
            break
        body += buffer
        file_size += len(buffer)
    return body

def parse_url(url):
    '''
    Возвращает кортеж вида (адрес, путь)
    '''
    u = urlparse(url)
    return u.netloc, u.path