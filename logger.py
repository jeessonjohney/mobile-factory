import logging

logger = logging.getLogger(__name__)


class BaseAppLogger:
    def log(self, message: str, level="info"):
        if hasattr(logger, level):
            method = getattr(logger, level)
            if callable(method):
                method(message)
            else:
                print(f"{level} is not callable.")
        else:
            print(f"{level} method not found in the object.")
