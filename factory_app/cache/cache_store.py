import threading


class GlobalStore:
    def __init__(self):
        self.cache = {}
        self.lock = threading.Lock()

    def set(self, key, value):
        with self.lock:
            self.cache[key] = value

    def get(self, key):
        with self.lock:
            return self.cache.get(key)

    def clear(self):
        with self.lock:
            self.cache.clear()

    def remove(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]


store = GlobalStore()


def flush():
    with store.lock:
        store.cache.clear()
