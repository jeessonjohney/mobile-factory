from starlette.requests import Request
from ..http import BaseFactoryAppEndpoint
from ..cache.cache_store import store
from ..api.validators import *
from json.decoder import JSONDecodeError


class Order(BaseFactoryAppEndpoint):
    async def post(self, request: Request) -> dict:
        mobile_parts = store.get("mobile_parts")
        try:
            data = await request.json()

            result = validate_order_request(data)

            if isinstance(result, str):
                return await self.write_error_response({"error": result})

            components = data.get("components", [])

            product_names = []
            product_prices = {
                product["id"]: float(product["price"]) for product in mobile_parts
            }

            product_types = set()
            total_price = 0.0
            # Can optmisise this by updating the cached config structure.
            for component_id in components:
                for product in mobile_parts:
                    if product["id"] == component_id:
                        product_names.append(product["name"])
                        product_type = product["type"]
                        if product_type in product_types:
                            return await self.write_error_response(
                                {
                                    "error": "Invalid order: Only one type of each product is allowed."
                                }
                            )
                        product_types.add(product_type)
                        total_price += product_prices[component_id]
                        break
                else:
                    return await self.write_error_response(
                        {"error": f"Invalid component ID: {component_id}"}
                    )

            required_types = {"screen", "camera", "port", "os", "body"}

            if product_types != required_types:
                return await self.write_error_response(
                    {
                        "error": "Invalid order: All product types (screen, camera, port, os, body) must be present."
                    }
                )

            output = {
                "order_id": 1,  # just a placeholder. Not sure whether any implementation required as part of assesment,
                "total": total_price,
                "parts": product_names,
            }
        except JSONDecodeError as exc:
            return await self.write_error_response(
                {
                    "error": "Invalid Order: Unable to parse request body. Must be a valid JSON"
                }
            )
        return await self.write_success_response(output)
