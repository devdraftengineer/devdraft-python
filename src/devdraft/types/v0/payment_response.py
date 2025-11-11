# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PaymentResponse"]


class PaymentResponse(BaseModel):
    id: str
    """Payment ID"""

    amount: float
    """The amount charged"""

    currency: str
    """The currency code"""

    status: str
    """Payment status"""

    timestamp: str
    """Timestamp of the payment"""
