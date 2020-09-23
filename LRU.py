class lru:

    def __init__(self, size):
        self.size = size
        self.lru = []
        self.lruCache = {}
