from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse
import typing


class BaseFactoryAppEndpoint(HTTPEndpoint):

    """
    Pagination must be done here
    """

    async def write_success_response(
        self, response: typing.Union[dict, list], status_code=200
    ) -> JSONResponse:
        data = {"status": "success", "data": response}
        response = JSONResponse(data, status_code=status_code)
        return response

    async def write_error_response(
        self, response: typing.Union[dict, list], status_code=400
    ) -> JSONResponse:
        data = {"status": "error", "data": response}
        response = JSONResponse(data, status_code=status_code)
        return response
