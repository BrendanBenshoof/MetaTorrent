import requests
import json


def init():
    global MT
    if not 'MT' in globals():
        with open("./config.json", "r") as fp:
            config = json.load(fp)
            MT = MetaTorrent(config)
    return MT


class MetaTorrent(object):

    def __init__(self, config):
        self.info = config['info']
        self.peers = config['peers']
        self.db = config['db']
        self.k = config['k']
