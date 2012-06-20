# -*- coding: utf-8 -*-

from vkmount import db, network

data = {} # path: data

def read(path, size, offset):
    if path in data:
        return data[path][offset:size + offset]
    else:
        data[path] = network.get_file([ track for track in db.tracks if track.name == path[1:]][0].url)
