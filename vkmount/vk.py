# -*- coding: utf-8 -*-
import urllib2
import json

class CallMethodError(Exception):
    def __init__(self, error_code, error_msg):
        self.code = int(error_code)
        self.msg = error_msg

    def __str__(self):
        return "{0}\nError Code: {1}".format(self.msg, self.code)



token = "4993c9fa4b15bf764b15bf76c34b383b6c44b144b14bf7e4d89c58d4fbcd20d"

def call_method(method_name, params={}, params_str=""):
    '''
    sample url - https://api.vk.com/method/audio.search?q=slozhnie&access_token=

    >>> Client().call_method("users.get", {"uids": "42366604"})
    [{u'first_name': u'Safsd', u'last_name': u'Sdfsdf', u'uid': 42366604}]

    >>> Client().call_method("users.get", {"uids": "0"})
    Traceback (most recent call last):
        ...
    CallMethodError: Invalid user id
    Error Code: 113
    '''
    if params:
        params_str = reduce(lambda x, y: x + y, [ key + "=" + str(params[key]) + "&" for key in params ])

    request = urllib2.Request("https://api.vk.com/method/{0}?{1}access_token={2}".format(
        method_name, params_str, token
    ))

    result_json = urllib2.urlopen(request)
    result = json.load(result_json)
    if "response" in result:
        return result['response']
    elif "error" in result:
        raise CallMethodError(result['error']['error_code'], result['error']['error_msg'])


def audio_search(query, sort = 2, count = 100, offset = 0):
    '''
    Выполняет глобальный поиск по аудиозаписям
    '''
    tracks = call_method("audio.search", {"q": query, "count": count})[1:]
    return tracks

def audio_get():
    '''
    Возвращает список аудиозаписей пользователя
    '''
    return call_method("audio.get")