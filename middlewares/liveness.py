import re
import time

from starlette.responses import JSONResponse
from starlette.routing import request_response
from starlette.types import ASGIApp, Receive, Scope, Send

path_regex = re.compile(r"^\/time(\/)?$")


async def timestamp(request):
    return JSONResponse({"timestamp": time.time()})


class LivenessMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            match = path_regex.match(scope.get("path"))
            if match:
                await request_response(timestamp)(scope, receive, send)
            else:
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)
