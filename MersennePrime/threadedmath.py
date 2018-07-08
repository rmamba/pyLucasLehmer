import threading
import math

class mul(threading.Thread):
    def __init__(self, idx, n, m):
        threading.Thread.__init__(self)
        self.idx = idx
        self.n = n
        self.m = m
        self.r = None

    def run(self):
        r = self.n * self.m
        self.r = []
        self.r.append(r % 256)
        while r>255:
            r = int(math.floor(r / 256))
            self.r.append(r % 256)

class sub(threading.Thread):
    def __init__(self, idx, n, m):
        threading.Thread.__init__(self)
        self.idx = idx
        self.n = n
        self.m = m
        self.r = None

    def run(self):
        self.r = self.n - self.m
        # self.r = []
        # self.r.append(r % 256)
        # while r>255:
        #     r = int(math.floor(r / 256))
        #     self.r.append(r % 256)
        # if r>0:
        #     self.r.append(r)
