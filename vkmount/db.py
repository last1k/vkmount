# -*- coding: utf-8 -*-

from vkmount import vk as vk, network

cur = None
tracks = []

class DBConnectionNotInit(Exception):
    pass

class Track():
    def __init__(self, audio_id, name, url, size = 0):
        self.audio_id = audio_id
        self.name = name
        self.url = url
        self.size = size

    def update(self):
        #TODO Обновляет информацию по треку (например url может меняться)
        pass


def init():
    #TODO сохранение базы треков (соответствие aid имени и ссылки на файл)
    #conn = sqlite3.connect(os.getenv('HOME')+'/.vkmount/audio.db')
    #cur = conn.cursor()
    for track in vk.audio_get():
        tracks.append(Track(
            track['aid'],
            track['artist'] + ' - ' + track['title'] + '.mp3',
            track['url'],
            network.get_size(track['url'])
        ))

def get_audio_info(audio_id):
    pass

def get_user_audio():
    pass