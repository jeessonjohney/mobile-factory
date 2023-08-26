from .cache import cache_store
from .utils import load_json_file
from config import MOBILE_PARTS_CONFIG_FILE_PATH, MOBILE_PARTS_CACHE_INTERVAL
from worker import Scheduler
from logger import BaseAppLogger


class Server(BaseAppLogger):
    def __init__(self):
        self.scheduler = Scheduler()

    def start(self):
        self.set_mobile_part_config()
        self.scheduler.schedule_task(
            self.set_mobile_part_config, interval_seconds=MOBILE_PARTS_CACHE_INTERVAL
        )

    def set_mobile_part_config(self):
        self.log(f"Setting mobile configuration from {MOBILE_PARTS_CONFIG_FILE_PATH}")
        mobile_parts = load_json_file(MOBILE_PARTS_CONFIG_FILE_PATH)
        if not mobile_parts:
            raise Exception(
                f"Unable to load mobile part configuration file from {MOBILE_PARTS_CONFIG_FILE_PATH}"
            )
        cache_store.store.set("mobile_parts", mobile_parts)

    def close(self):
        self.log(f"Initialised server termination")
        cache_store.flush()
