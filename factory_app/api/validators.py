from pydantic import BaseModel
from typing import List


class OrderRequest(BaseModel):
    components: List[str]


def validate_order_request(data: dict) -> str:
    try:
        order_data = OrderRequest(**data)
    except Exception as exc:
        return "Invalid request body. Must be a valid JSON"

    if not order_data.components:
        return "Invalid order: At least one component must be specified."

    for component_id in order_data.components:
        if not isinstance(component_id, str):
            return "Invalid component ID: Must be str."
