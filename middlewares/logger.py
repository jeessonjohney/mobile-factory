import logging
import time
from starlette.middleware.base import BaseHTTPMiddleware
from logger import BaseAppLogger

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LoggingMiddleware(BaseHTTPMiddleware, BaseAppLogger):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()

        log_message = f"{request.method} {request.url.path} - {response.status_code} - {end_time - start_time:.6f}s"
        self.log(log_message, "info")
        return response
