import time
import datetime


class ScrapperMeta:

    def __init__(self):
        self.id = str(time.time())
        self.last_seen = self.refresh_last_seen()

    def refresh_last_seen(self):
        self.last_seen = datetime.datetime.now()
        return self.last_seen

    def to_json(self):
        return '{"id" : "%s", "last_seen": "%s"}' % (self.id, self.last_seen)
