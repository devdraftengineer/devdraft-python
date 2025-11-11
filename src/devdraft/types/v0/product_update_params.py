# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    currency: Literal["USD", "EUR", "GBP", "CAD", "AUD", "JPY"]
    """Currency code for the price. Defaults to USD if not specified."""

    description: str
    """Detailed description of the product.

    Supports markdown formatting for rich text display.
    """

    images: SequenceNotStr[str]
    """Array of image URLs"""

    name: str
    """Product name as it will appear to customers. Should be clear and descriptive."""

    price: float
    """Product price in the specified currency. Must be greater than 0."""

    product_type: Annotated[str, PropertyInfo(alias="productType")]
    """Product type"""

    quantity: float
    """Quantity available"""

    status: str
    """Product status"""

    stock_count: Annotated[float, PropertyInfo(alias="stockCount")]
    """Stock count"""

    type: str
    """Product type"""

    unit: str
    """Unit of measurement"""

    weight: float
    """Weight of the product"""
