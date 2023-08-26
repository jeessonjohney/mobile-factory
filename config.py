from dotenv import load_dotenv
import os

load_dotenv()

API_VERSION = os.getenv("API_VERSION")
DEBUG = os.getenv("DEBUG")
MOBILE_PARTS_CONFIG_FILE_PATH = os.getenv("MOBILE_PARTS_CONFIG_FILE_PATH")
MOBILE_PARTS_CACHE_INTERVAL = int(os.getenv("MOBILE_PARTS_CACHE_INTERVAL"))
