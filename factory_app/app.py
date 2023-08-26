from middlewares.liveness import LivenessMiddleware
from middlewares.logger import LoggingMiddleware
from middlewares.validation import ValidationMiddleware
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from .server import Server
from config import DEBUG
from .urls import url_patterns

server = Server()

server.start()

app = Starlette(debug=DEBUG, on_shutdown=[server.close])

app.add_middleware(LivenessMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(ValidationMiddleware)

for url in url_patterns:
    app.add_route(url[0], url[1])


@app.exception_handler(404)
async def not_found(request, exc):
    return JSONResponse(
        {"status": "error", "message": "Page not found"}, status_code=exc.status_code
    )


@app.exception_handler(405)
async def method_not_allowed(request, exc):
    return JSONResponse(
        {"status": "error", "message": "Method Not Allowed"}, status_code=405
    )


@app.exception_handler(500)
async def server_error(request, exc):
    return JSONResponse(
        {"status": "error", "message": "Server error"},
        status_code=500,
    )
