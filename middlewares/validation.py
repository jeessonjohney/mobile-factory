from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import request_response
from starlette.types import ASGIApp, Receive, Scope, Send


class ValidationMiddleware(Middleware):
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)
        request = Request(scope)
        if request.headers.get("Content-Type") != "application/json":
            await request_response(contentTypeError)(scope, receive, send)
        await self.app(scope, receive, send)


def contentTypeError(request):
    return JSONResponse(
        {"error": "Invalid content type. Expecting application/json"}, status_code=400
    )
