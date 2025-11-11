# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TestPaymentRefundResponse"]


class TestPaymentRefundResponse(BaseModel):
    __test__ = False
    id: str
    """Refund ID"""

    amount: float
    """The amount refunded"""

    payment_id: str = FieldInfo(alias="paymentId")
    """Original payment ID"""

    status: str
    """Refund status"""

    timestamp: str
    """Timestamp of the refund"""
