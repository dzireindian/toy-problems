class lru:

    def __init__(self, size):
        self.size = size
        self.lru = []
        self.lrucache = {}

    def get(self, key):
        if key in self.lru:
            return self.lrucache[key]
        else:
            return None

    def put(self, key):
        value = "www."+str(key)+".com"
        if(len(self.lru) < self.size):
            if key in self.lru:
                self.lru.remove(key)
                self.lru.append(key)
                self.lrucache[key] = value
            else:
                self.lru.append(key)
                self.lrucache[key] = value
        else:
            val = self.lru.pop(0)
            self.lru.append(key)
            del self.lrucache[val]
            self.lrucache[key] = value

    def get_cache(self):
        l = []
        for k in reversed(self.lru):
            l.append(k+" : "+self.lrucache[k])
        return l
