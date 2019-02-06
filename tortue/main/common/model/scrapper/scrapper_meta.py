import time
import datetime


class ScrapperMeta:
    def __init__(self):
        self.id = str(time.time())
        self.last_seen = self.refresh_last_seen()

    def refresh_last_seen(self) -> datetime:
        self.last_seen = datetime.datetime.now()
        return self.last_seen

    def to_json(self) -> dict:
        return {"id": self.id, "last_seen": str(self.last_seen)}
