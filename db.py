import json
import time


class TorrentDataBase(object):

    def __init__(self, path):
        self.path = path
        with open(self.path, "r") as fp:
            self.data = json.load(fp)

    def search(self, filter_lambda):
        for t in self.data:
            if filter_lambda(t):
                yield t

    def add(self, t):
        t['time'] = time.time()
        self.data[t['BTIH']] = t

    def save(self):
        with open(self.path, "w") as fp:
            json.dump(self.data, fp)
